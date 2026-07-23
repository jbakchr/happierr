# happierr

Translate technical failures into human encouragement.

happierr is a CLI tool that helps developers understand errors without feeling defeated by them.

It doesn't hide errors.

It doesn't pretend mistakes don't matter.

It doesn't tell developers that everything is fine.

Instead, happierr helps developers understand:

- what happened
- why it happened
- what to try next

while also reminding them that errors are a normal part of software development.

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

Given a Python error such as:

```text
ModuleNotFoundError:
No module named 'requests'
```

happierr preserves the original error and then explains it in a friendlier and more actionable format.

Example:

```text
╭──────────── Original Error ────────────╮
│ ModuleNotFoundError:                   │
│ No module named 'requests'             │
╰────────────────────────────────────────╯

╭───────────── happierr ─────────────────╮
│ 🙂 Good news                           │ 
│                                        │
│ Error Type                             │
│ ModuleNotFoundError                    │
│                                        │
│ What Happened                          │
│ → Python attempted to import a         │
│   module that could not be found.      │
│                                        │
│ → The module "requests" is not         │
│   installed.                           │
│                                        │
│ Why This Happens                       │
│ → This is one of the most common       │
│   Python errors developers encounter.  │
│                                        │
│ What To Try Next                       │
│ → pip install requests                 │
╰────────────────────────────────────────╯
```

The goal is not to replace the original error.

The goal is to help developers understand it.

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

### Preserve The Original Error

Errors contain useful information.

happierr should help developers understand errors, not hide them.

The original error is displayed alongside happierr's interpretation.

---

## Current Workflow

happierr follows a simple workflow:

```text
Error
    ↓
Recognize
    ↓
Explain
    ↓
Encourage
    ↓
Suggest Next Step
```

For example:

```text
ModuleNotFoundError
```

becomes:

```text
What Happened

↓

Why This Happens

↓

What To Try Next
```

---

## Example Usage

Pipe output directly into happierr:

```bash
python app.py 2>&1 | happierr
```

Or:

```bash
happierr < error.txt
```

---

## Current Features

### Error Recognition

✅ ModuleNotFoundError

---

### Error Explanation

✅ Explain what happened

✅ Explain why it happened

✅ Explain what to try next

---

### Encouragement

✅ Friendly and supportive language

✅ Error normalization

✅ Learning-oriented explanations

---

### Terminal Output

✅ Preserve original error

✅ Colorized output

✅ Rich panels

✅ Structured sections

---

## Current Scope

Version 1 currently focuses on Python.

Planned support includes:

- ImportError
- SyntaxError
- FileNotFoundError

Future versions may support:

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

✅ normalize technical failures

✅ bring a little more humanity to terminal output

✅ help developers build confidence

---

## Non-Goals

happierr is NOT:

- an AI coding agent
- an automated debugging tool
- an IDE
- a compiler replacement
- a stack trace replacement
- a linter
- a static analysis platform

The original error remains important.

happierr simply helps developers understand it.

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

If happierr can help even a few developers feel more confident when facing technical problems, it has achieved its purpose.

---

## Inspiration

Software development already has plenty of tools that point out what is wrong.

happierr exists to help developers understand what went wrong while remembering something equally important:

```text
The code failed.

Not the developer.
```