# Django REST API for Teams and Members

This Django REST API allows users to manage teams and their members. With this API, users can create, read, update, and delete both teams and their associated members.


## Features

1. Teams: Manage a list of teams.
   - Create new teams.
   - Retrieve a list of all teams or details about a specific team.
   - Update team details.
   - Delete a team.

2. Members: Manage members within teams.
   - Add a member to a specific team.
   - Retrieve a list of all members or details about a specific member.
   - Update member details.
   - Remove a member from a team.

## Examples

Here are some example usages of the API:

Create a new team:
```bash
POST /api/teams/
{
    "name": "Development"
}
```

Retrieve all teams:
```bash
GET /api/teams/
```

Add a member to a team:

```bash
POST /api/members/
{
    "name": "John",
    "surname": "Doe",
    "email": "johndoe@example.com",
    "team": 1
}
```

Retrieve members of a specific team:
```bash
GET /api/teams/1/members/
```


## Setup Instructions
### Prerequisites
- Python (3.6 or newer recommended)
- pip
- Virtualenv (optional, but recommended)

### Steps

1. Clone the repository:
```bash
git clone https://github.com/yourusername/yourrepositoryname.git
cd Teams
```

2. Set up a virtual environment (optional, but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Run the development server:
```bash
python manage.py runserver
```

Now, you should be able to access the API at http://127.0.0.1:8000/.
