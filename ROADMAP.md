# ROADMAP

happierr is a CLI tool that helps developers understand errors.

It does not hide errors.

It does not replace stack traces.

It does not pretend mistakes do not exist.

Its purpose is to help developers understand:

- what happened
- why it happened
- what to try next

while remembering:

```text
The code failed.

Not the developer.
```

---

## Project Vision

Most developer tools focus on:

```text
What went wrong?
```

happierr focuses on:

```text
What happened?

Why did it happen?

What should I try next?
```

The goal is not dependency.

The goal is confidence.

The long-term vision is to help developers move from:

```text
Oh no.
```

to:

```text
Okay.

I understand this.
```

and eventually:

```text
I already know what this error means.
```

---

## Core Philosophy

### The Error Is Not The Developer

Technical failures happen to everyone.

Errors are not evidence that someone is a bad developer.

Errors are evidence that someone is developing.

happierr should continuously reinforce this idea.

---

### Explain Before Fixing

Before suggesting solutions, explain the problem.

Understanding creates confidence.

Confidence reduces panic.

---

### Preserve Before Interpreting

The original error should always remain visible.

Trust comes from transparency.

happierr should help developers understand errors without hiding them.

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

## Current Architecture

```text
stdin
    ↓
pattern matching
    ↓
response creation
    ↓
rendering
```

Current structure:

```text
commands/
patterns/
messages/
renderers/
models/
```

---

## Current State

Status:

🟢 Active Development

Implemented:

✅ CLI entry point

✅ stdin support

✅ Rich rendering

✅ response model

✅ original error preservation

✅ structured explanations

✅ colorized output

---

### Supported Errors

✅ ModuleNotFoundError

✅ ImportError

✅ SyntaxError

✅ FileNotFoundError

---

### Current Output Structure

```text
Original Error

↓

Error Type

↓

What Happened

↓

Why This Happens

↓

What To Try Next
```

---

## Development Roadmap

### Phase 1 — Understand Errors

Status:

✅ In Progress

Goal:

Recognize common Python errors and explain them clearly.

Current focus:

✅ ModuleNotFoundError

✅ ImportError

✅ SyntaxError

✅ FileNotFoundError

Future candidates:

- ValueError
- TypeError
- AttributeError
- KeyError
- NameError
- IndexError
- ZeroDivisionError

Success Criteria:

A developer immediately understands:

- what happened
- why it happened
- what to try next

---

### Phase 2 — Improve Explanations

Status:

🟡 Next

Goal:

Provide deeper explanations while remaining concise.

Example:

Instead of:

```text
Module not found.
```

Explain:

```text
Python attempted to import a package
that could not be found in the
current environment.
```

Potential additions:

- clearer wording
- more educational explanations
- better mental models
- related concepts

Success Criteria:

Understanding improves without increasing complexity.

---

### Phase 3 — Developer Learning Tool

Status:

🔲 Planned

Goal:

Turn common errors into learning opportunities.

Example:

```text
ModuleNotFoundError

Related Concepts

• Python packages
• pip
• virtual environments
```

The objective is not only recovery.

The objective is learning.

Success Criteria:

Developers gain transferable knowledge rather than merely solving the current error.

---

### Phase 4 — Error Library

Status:

🔲 Planned

Goal:

Allow developers to explore errors without first encountering them.

Potential command:

```bash
happierr explain ModuleNotFoundError
```

Example use cases:

```bash
happierr explain SyntaxError

happierr explain ImportError
```

Success Criteria:

Developers can learn proactively instead of reactively.

---

### Phase 5 — Examples

Status:

🔲 Planned

Goal:

Provide examples of common mistakes that cause each error.

Potential command:

```bash
happierr examples ModuleNotFoundError
```

Example output:

```text
Example 1

import requests

Package not installed.

--------------------

Example 2

from panda import DataFrame

Package name misspelled.
```

Success Criteria:

Developers recognize common patterns before encountering them.

---

### Phase 6 — Language Expansion

Status:

🔲 Future

Goal:

Expand beyond Python.

Potential languages:

- JavaScript
- TypeScript
- Go
- Rust
- Java
- C#

Important:

Python support should feel complete before additional languages are considered.

Success Criteria:

happierr remains useful regardless of primary programming language.

---

## Future Ideas

These ideas are intentionally lower priority.

### Related Concepts

Show concepts connected to an error.

Example:

```text
ModuleNotFoundError

Related Concepts

• packages
• pip
• virtual environments
```

---

### Error Collections

Curated groups of common beginner errors.

Examples:

```text
Import errors

File errors

Syntax errors
```

---

### Onboarding Packs

Potential use in teaching and onboarding.

Not currently a focus.

---

## Explicit Non-Goals

happierr is NOT:

- an AI coding agent
- a debugger
- a compiler
- a linter
- a static analysis platform
- a stack trace replacement
- a code generation tool
- an IDE

happierr complements existing tools.

It does not replace them.

---

## Things We Are Intentionally Avoiding

For now:

❌ AI-generated explanations

❌ automatic code fixes

❌ debugging workflows

❌ telemetry

❌ error statistics

❌ complex analysis engines

Reason:

These features move happierr away from its core purpose:

```text
Understanding > Panic
```

---

## Definition Of Success

A developer sees:

```text
Traceback...
```

runs:

```bash
happierr
```

and thinks:

```text
Okay.

I understand what happened.
```

Even greater success:

The developer begins recognizing and understanding common errors before running happierr.

The goal is not dependency.

The goal is growth.

The best outcome is that developers internalize the explanations and confidence that happierr helps provide.

Because:

```text
The code failed.

Not the developer.
```
