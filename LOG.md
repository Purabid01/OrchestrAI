## Day 1 — 06-08-2026


**Branch:** day-01/toolchain-setup
**Commit:** b4fe472

**What I did: Today I setup my local env like install all the dependencies like puthon, git, uv and then and create and write readme and log.md file for summary**

**What broke or confused me: I installed python latest version(3.14.4) but for this project with langraph kinda techstack we need python3.12 version. Explanation: Issue 1: Python 3.14.4  That's too new. The workbook targets Python 3.12. Libraries like LangGraph, SQLAlchemy async, and the Anthropic SDK are tested against 3.12. On 3.14 we may hit subtle incompatibilities in months 3-4 that produce confusing errors with no Stack Overflow answers, because 3.14 is brand new.we need to install Python 3.12 alongside our current version and use it as the project interpreter. Do not uninstall 3.14 — just add 3.12.**





**What I still don't understand: 1. why cant we use our system directly instead we want venv**
