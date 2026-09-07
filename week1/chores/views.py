from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Household, Roommate, Chore
from .forms import ChoreForm


def _get_default_household():
    """MVP helper: return the first household, or create a default one."""
    household = Household.objects.first()
    if household is None:
        household = Household.objects.create(
            name="My Apartment",
            created_by=None,
        )
    return household


def chore_list(request):
    household = _get_default_household()
    chores = Chore.objects.filter(household=household).select_related("assigned_to")
    return render(
        request,
        "chores/list.html",
        {"household": household, "chores": chores},
    )


def chore_create(request):
    household = _get_default_household()
    if request.method == "POST":
        form = ChoreForm(request.POST, household=household)
        if form.is_valid():
            chore = form.save(commit=False)
            chore.household = household
            chore.save()
            messages.success(request, f"Added '{chore.title}'")
            return redirect("chores:list")
    else:
        form = ChoreForm(household=household)
    return render(
        request,
        "chores/create.html",
        {"household": household, "form": form},
    )


def chore_toggle(request, pk):
    chore = get_object_or_404(Chore, pk=pk)
    if request.method == "POST":
        if chore.status == Chore.STATUS_OPEN:
            chore.status = Chore.STATUS_DONE
        else:
            chore.status = Chore.STATUS_OPEN
        chore.save()
    return redirect("chores:list")
