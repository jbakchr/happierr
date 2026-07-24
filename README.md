# happierr

Translate technical failures into understanding.

happierr is a CLI tool that helps developers understand errors without feeling defeated by them.

It does not hide errors.

It does not replace stack traces.

It does not pretend mistakes do not matter.

Instead, happierr helps developers understand:

- what happened
- why it happened
- what to try next

while reminding them of something equally important:

> The code failed.
>
> Not the developer.

---

# Why?

Software developers spend much of their day receiving feedback like:

```text
SyntaxError

ImportError

ModuleNotFoundError

FileNotFoundError

TypeError

ValueError

AttributeError
```

These messages are often technically correct.

But they are not always easy to understand.

Over time it can become easy to interpret technical failures as personal failures:

```text
I failed.

I'm behind.

I'm not good enough.

I don't understand this.
```

happierr is built on a different idea:

```text
Errors are evidence that someone
is developing.

Not evidence that someone
is a bad developer.
```

---

# What happierr Does

Given an error:

```bash
python app.py 2>&1 | happierr
```

happierr preserves the original error and provides a structured explanation.

Example:

```text
ImportError:
cannot import name 'potato' from 'math'
```

becomes:

```text
Error Type

ImportError

What Happened

Python successfully found the module.

The requested name could not be imported.

Why This Happens

The name may not exist.

The name may be misspelled.

What To Try Next

Check the spelling.

Review the documentation.
```

The goal is not to replace the original error.

The goal is to help developers understand it.

---

# Beyond Error Interpretation

happierr is gradually becoming a learning tool.

You can explore supported error guides:

```bash
happierr errors
```

and learn about a specific error:

```bash
happierr explain TypeError
```

Example:

```bash
happierr explain ModuleNotFoundError
```

This provides:

- What Is It
- Mental Model
- Common Causes
- What To Try Next
- Related Concepts

The objective is not merely to recover from an error.

The objective is to understand it.

---

# Core Philosophy

## Understanding Before Fixing

Many errors are technically correct but difficult to understand.

Before suggesting solutions, happierr explains what an error means.

---

## Preserve Before Interpreting

The original error should always remain visible.

Trust comes from transparency.

---

## Learning Over Judgement

Errors should be treated as learning opportunities.

Not as evidence of failure.

---

## Encourage Without Pretending

Bad:

```text
Everything is amazing!
```

Good:

```text
This is a common error.

Here's what happened.

Here's what you can try next.
```

---

## The Error Is Not The Developer

The central belief behind happierr is:

```text
The code failed.

Not the developer.
```

---

# How It Works

For error interpretation:

```text
Error
    ↓
Recognize
    ↓
Interpret
    ↓
Explain
    ↓
Suggest Next Step
```

For learning:

```text
Browse
    ↓
Learn
    ↓
Understand
```

Examples:

```bash
happierr errors
```

```bash
happierr explain TypeError
```

---

# Installation

```bash
pip install happierr
```

---

# Usage

Interpret an error:

```bash
python app.py 2>&1 | happierr
```

or:

```bash
happierr < error.txt
```

Browse supported guides:

```bash
happierr errors
```

Learn about an error:

```bash
happierr explain TypeError
```

---

# Usage Examples

## Interpret an Error

Run a program and pipe the output into happierr:

```bash
python app.py 2>&1 | happierr
```

Example:

```bash
python broken.py 2>&1 | happierr
```

happierr preserves the original error and explains:

- what happened
- why it happened
- what to try next

---

## Explain an Error

Learn about a specific Python error:

```bash
happierr explain TypeError
```

or:

```bash
happierr explain ModuleNotFoundError
```

Each guide includes:

- What Is It
- Mental Model
- Common Causes
- What To Try Next
- Related Concepts

Example:

```bash
happierr explain KeyError
```

---

## Browse Available Guides

See all currently available error guides:

```bash
happierr errors
```

This displays the supported learning guides grouped by category.

Example:

```bash
happierr errors
```

---

## Learn Before Encountering An Error

happierr can be used proactively as a learning tool.

For example:

```bash
happierr errors
```

followed by:

```bash
happierr explain ValueError
```

allows developers to learn about common errors before they encounter them in real projects.

---

## Read Saved Errors

Interpret a saved traceback or error log:

```bash
happierr < error.txt
```

Useful when:

- sharing errors
- reviewing logs
- learning from previous failures

---

## Example Learning Workflow

```bash
happierr errors
```

Find an interesting error:

```bash
happierr explain TypeError
```

Encounter the error in real code:

```bash
python app.py 2>&1 | happierr
```

Result:

```text
Error
    ↓
Understanding
    ↓
Learning
```

---

# Supported Error Guides

Currently included:

## Import Errors

- ModuleNotFoundError
- ImportError

## Language Errors

- SyntaxError
- NameError

## Type & Value Errors

- TypeError
- ValueError

## Object & Collection Errors

- AttributeError
- KeyError
- IndexError

## File Errors

- FileNotFoundError

---

# Current Features

## Error Interpretation

✅ Preserve original errors

✅ Explain what happened

✅ Explain why it happened

✅ Suggest what to try next

✅ Learning-oriented explanations

---

## Error Guides

✅ Browse available guides

✅ Learn about specific errors

✅ Mental models

✅ Common causes

✅ Related concepts

✅ Suggested next steps

---

## Terminal Experience

✅ Rich formatting

✅ Structured output

✅ Learning-focused design

✅ Clear visual hierarchy

---

# Current Scope

Version 1 focuses exclusively on Python.

Potential future language support:

- JavaScript
- TypeScript
- Go
- Rust
- Java
- C#

Only after Python support feels genuinely solid.

---

# Non-Goals

happierr is NOT:

- an AI coding agent
- a debugger
- a compiler replacement
- a stack trace replacement
- a linter
- a code generation tool
- a static analysis platform
- an IDE

The goal is understanding.

Not automation.

Not AI-generated fixes.

---

# Project Goals

happierr aims to:

✅ make common errors easier to understand

✅ help developers build mental models

✅ reduce unnecessary frustration

✅ encourage learning

✅ normalize technical failures

✅ improve confidence

✅ teach concepts, not just fixes

---

# Long-Term Vision

The goal is not dependency.

The goal is growth.

Success looks like:

```text
Okay.

I understand what happened.
```

Even greater success:

```text
I already know what this error means.
```

because the developer learned it from previous encounters.

The best outcome is that developers eventually need happierr less because they have internalized the understanding it helped provide.

---

# Inspiration

Software development already has many tools that point out what is wrong.

happierr exists to help developers understand what happened, why it happened, and what to try next.

Because:

```text
Understanding reduces panic.

The code failed.

Not the developer.
```
