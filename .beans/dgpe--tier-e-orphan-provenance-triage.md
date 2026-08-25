---
# dgpe
title: 'Tier E: orphan witnesses — producer missing from disk'
status: todo
type: task
priority: normal
created_at: 2026-08-18T21:00:00Z
updated_at: 2026-08-18T21:00:00Z
---

Parent dgap. 186 witnesses whose producer script is not on disk (scriptFile names a file that
does not exist, or the name-guess convention finds nothing). A derivation chain CANNOT be
honestly authored against a producer that no longer exists — the script: note would cite a
path the validator resolves to nothing, and the provenance claim would be empty.

Per witness, exactly one of:
  (a) recover the producer (renamed / moved / lives outside computations/) and fix scriptFile;
  (b) retire the witness to _deprecated/ with a note saying why provenance was lost;
  (c) regenerate from a current producer if the quantity is still wanted.

At least 3 already self-report the loss: scriptFile reads
"(legacy — no matching producer found; provenance pending manual triage)".
List them: python3 computations/audits/derivation_gap_categorize.py --tier E-orphan
