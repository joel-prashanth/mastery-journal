# Mastery OS — Product Spec (v1)

## What it is
A personal tool for tracking my software mastery journey — logging study
sessions, seeing my streaks and progress, and eventually getting smart
recommendations on what to learn next.

## The problem it solves
Without tracking, it's easy to lose momentum on a multi-year learning path
and hard to see real progress. Mastery OS makes the practice of studying
itself visible and measurable.

## v1 scope — what's IN
- Log a study session: hours studied + date
- View all logged sessions
- Current streak (consecutive days studied)
- Longest streak ever
- Total hours logged
- Runs locally via the terminal
- Data persists to a local file between runs

## Explicitly OUT of v1 (deferred, not forgotten)
- Database storage → Unit 2
- Web API → Unit 3
- Web dashboard (frontend) → Unit 4
- Authentication / multi-user support → Unit 3
- Cloud deployment → Unit 6
- AI-powered recommendations → Unit 7

## Core user flow (v1)
1. Run the app.
2. Choose to log a new session (enter hours + today's date is captured
   automatically) or view stats.
3. See updated totals, current streak, and longest streak.
4. Exit; data is still there next time the app runs.

## Constraints
- Single user (me).
- Local-only — no network calls, no server, in v1.
- Terminal-based — no GUI until Unit 4.