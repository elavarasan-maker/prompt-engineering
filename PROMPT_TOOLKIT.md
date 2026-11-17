# Module 02 — Prompt Engineering & AI Productivity

## Prompt structure
Role + context + task + constraints + output format + quality checks.

### Zero-shot template
Task: {specific task}
Context: {background}
Audience: {audience}
Constraints: {length, tone, exclusions}
If information is missing, say what is missing. Do not invent facts.
Output format: {format}

### Few-shot method
Give 2–3 representative input/output examples, then the new input. Ensure examples are correct and demonstrate the requested pattern.

## Reusable workflows
- **Summarization:** summarize only supplied text; separate facts, decisions, risks and open questions.
- **Email:** draft using only supplied facts; do not invent names, dates, promises or attachments.
- **Resume:** improve wording but never invent metrics, tools or achievements; mark missing evidence as [add verified metric].
- **Coding:** explain cause, minimal fix and test; state assumptions and avoid unrelated edits.
- **Research:** create outline, search terms and source-quality criteria; never fabricate citations.

## Structured output
Prompting for JSON does not guarantee valid JSON. Parse and validate it in application code.
