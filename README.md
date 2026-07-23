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
> Not the developer.

---

## Why?

Software developers spend much of their day receiving feedback like:

```text
SyntaxError

ImportError

ModuleNotFoundError

FileNotFoundError

Build failed

Test failed

Unexpected exception
```

These messages are often technically correct.

But they are not always easy to understand.

After seeing thousands of errors over the course of a career, it can be easy to interpret them as:

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

Given an error, happierr preserves the original output and then explains it in a more approachable format.

For example:

```text
ImportError:
cannot import name 'potato' from 'math'
```

becomes:

```text
Error Type

ImportError

What Happened

→ Python successfully located the module.

→ The requested name could not be imported.

Why This Happens

→ The name may not exist.

→ The name may be misspelled.

→ The module may have changed.

What To Try Next

→ Check the spelling.

→ Review the module documentation.
```

The goal is not to replace the original error.

The goal is to help developers understand it.

---

## Core Philosophy

### Understanding Before Fixing

Many error messages are technically correct but difficult to understand.

Before suggesting solutions, happierr explains what the error means.

---

### Preserve Before Interpreting

The original error should always remain visible.

Errors contain useful information.

happierr helps developers understand those errors rather than hiding them.

---

### Learning Over Judgement

Errors should be treated as learning opportunities.

Not as evidence of failure.

---

### Encourage Without Pretending

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

### The Error Is Not The Developer

The central belief behind happierr is:

```text
The code failed.

Not the developer.
```

---

## How It Works

happierr follows a very simple workflow:

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

The focus is understanding.

Not debugging.

Not automation.

Not AI-generated fixes.

---

## Installation

```bash
pip install happierr
```

---

## Usage

Pipe stderr into happierr:

```bash
python app.py 2>&1 | happierr
```

Or:

```bash
happierr < error.txt
```

---

## Supported Errors

Currently supported:

### ModuleNotFoundError

Example:

```python
import requests
```

when the package is not installed.

---

### ImportError

Example:

```python
from math import potato
```

when the module exists but the requested name does not.

---

### SyntaxError

Example:

```python
print("hello"
```

when Python cannot understand the structure of the code.

---

### FileNotFoundError

Example:

```python
open("missing.txt")
```

when the requested file cannot be located.

---

## Current Features

### Error Recognition

✅ ModuleNotFoundError

✅ ImportError

✅ SyntaxError

✅ FileNotFoundError

---

### Error Interpretation

✅ Explain what happened

✅ Explain why it happened

✅ Suggest what to try next

✅ Preserve original errors

---

### Terminal Experience

✅ Rich panels

✅ Structured output

✅ Colorized rendering

✅ Learning-focused explanations

---

## Current Scope

Version 1 focuses exclusively on Python.

Future language support may include:

- JavaScript
- TypeScript
- Go
- Rust
- Java
- C#

Only after Python support feels solid.

---

## Non-Goals

happierr is NOT:

- an AI coding agent
- a debugger
- an IDE
- a compiler replacement
- a stack trace replacement
- a linter
- a code generation tool
- a static analysis platform

The original error remains important.

happierr simply helps developers understand it.

---

## Project Goals

happierr aims to:

✅ make common errors easier to understand

✅ provide practical next steps

✅ reduce unnecessary frustration

✅ encourage learning

✅ normalize technical failures

✅ improve developer confidence

✅ help developers build mental models of common errors

---

## Long-Term Vision

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

because the developer has learned from previous explanations.

The best outcome is that one day developers no longer need happierr because they have internalized the understanding that happierr helped provide.

---

## Inspiration

Software development already has many tools that point out what is wrong.

happierr exists to help developers understand what happened and what to try next without confusing technical failure with personal failure.

```text
The code failed.

Not the developer.
```

