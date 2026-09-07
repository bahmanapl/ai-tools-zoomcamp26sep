# Backlog — Shared Chore Manager MVP

## Task 1: Design and create the data models
- Create `Household` model (name, created_by)
- Create `Roommate` model (name, household FK, user FK)
- Create `Chore` model (title, household FK, assigned_to FK roommate, status, created_at)
- Status choices: Open / Done
- Add `__str__` methods for admin readability
- Run migrations to apply schema

## Task 2: Wire up URLs and views for the chore list
- Create `chores/urls.py` with route for the shared chore list
- Create view that fetches all chores for the current household
- Render a simple template showing each chore with its title, assignee, and Done checkbox
- Link the app into the project-level `urls.py`

## Task 3: Add chore creation flow
- Form to create a new chore (title + assignee dropdown)
- On submit, save chore to the current household with status=Open
- Redirect back to the chore list
- Show success feedback

## Task 4: Add chore completion flow
- POST endpoint to toggle a chore to Done
- Simple button or checkbox click marks chore as Done
- List persists across requests (no page refresh needed, or minimal)

## Task 5: Basic styling and templates
- Single base template for layout
- Chore list as a checklist (checkbox + title + assignee)
- Clean, minimal visual design
- Mobile-friendly

## Task 6: (Optional polish) Basic authentication stub
- Placeholder for household selection or login
- For MVP, hardcode or use a single test household
