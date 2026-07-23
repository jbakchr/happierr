# happierr

Translate technical failures into human encouragement.

happierr is a CLI tool that helps developers understand errors without feeling defeated by them.

It doesn't hide errors.

It doesn't pretend mistakes don't matter.

It doesn't tell developers that everything is fine.

Instead, happierr explains what happened, reminds developers that errors are a normal part of software development, and helps them take the next step.

---

## Why?

Software developers receive feedback all day long.

Much of that feedback looks like:

```text
SyntaxError
ImportError
ModuleNotFoundError
Build failed
Test failed
Unexpected exception
```

These messages are often correct.

But after seeing thousands of errors over the course of a career, it can be easy to internalize them as:

```text
I failed.

I'm behind.

I'm not good enough.

I don't understand this.
```

happierr is based on a simple idea:

```text
The code failed.

Not the developer.
```

Errors are not evidence that someone is a bad developer.

Errors are evidence that someone is developing.

---

## What happierr Does

Given an error message:

```text
ModuleNotFoundError:
No module named 'requests'
```

happierr might produce:

```text
🙂 Good news

Python successfully identified
the problem.

The module "requests"
isn't installed.

This is one of the most common
Python errors developers encounter.

Try:

pip install requests

You're likely only one command
away from resolving this issue.
```

The goal is to transform:

```text
Error
```

into:

```text
Understanding
```

and

```text
Discouragement
```

into:

```text
Encouragement
```

---

## Philosophy

### The Error Is Not The Developer

Technical failures happen to everyone.

From beginners to experienced developers.

happierr separates the error from the person.

---

### Explain Before Fixing

Many error messages are technically correct but difficult to understand.

happierr attempts to explain what happened in plain language before suggesting possible next steps.

---

### Encourage Without Pretending

happierr is not interested in fake positivity.

The goal is not:

```text
Everything is amazing!
```

The goal is:

```text
This error is normal.

Here's what it means.

Here's what you can try next.
```

---

### Learning Over Judgement

happierr treats errors as learning opportunities rather than evidence of failure.

---

## Example Usage

Run a program and pipe its output into happierr:

```bash
python app.py 2>&1 | happierr
```

Or:

```bash
happierr < error.txt
```

---

## Initial Scope

Version 1 focuses on Python.

Examples:

- ModuleNotFoundError
- ImportError
- SyntaxError
- FileNotFoundError

Future versions may support additional languages:

- JavaScript
- TypeScript
- Go
- Java
- Rust
- C#

---

## Project Goals

happierr aims to:

✅ make common errors easier to understand

✅ provide practical next steps

✅ reduce unnecessary frustration

✅ encourage learning

✅ remind developers that errors are normal

✅ bring a little more humanity to terminal output

---

## Non-Goals

happierr is NOT:

- an AI coding agent
- an automated debugging tool
- an IDE
- a compiler replacement
- a stack trace analyzer
- a tool that hides errors

The original error remains important.

happierr simply helps developers respond to it.

---

## Long-Term Vision

The goal is not to eliminate errors.

The goal is not to eliminate frustration entirely.

The goal is to help developers look at an error and think:

```text
Okay.

I understand this.

Let's figure it out.
```

instead of:

```text
Oh no.

What now?
```

If happierr can make even a few developers feel a little more confident when facing technical problems, it has achieved its purpose.

---

## Inspiration

Software development already has plenty of tools that point out what is wrong.

happierr exists to help developers remember that making mistakes is a normal part of learning, building, and growing.

Because:

```text
The code failed.

Not the developer.
```
