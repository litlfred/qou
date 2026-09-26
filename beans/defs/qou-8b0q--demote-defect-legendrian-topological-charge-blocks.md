---
# qou-8b0q
title: Demote defect-legendrian + topological-charge blocks to conjecture (post-q407)
status: todo
type: task
created_at: 2026-08-21T15:10:31Z
updated_at: 2026-08-21T15:10:31Z
---

q407 converted the vacuous 'theorem (h:P):P:=h' Lean siblings of these two blocks to honest 'def : Prop' (Pattern C), clearing the self-assuming-projection flag. But the .ts block kinds are still 'proposition' (defect-legendrian-knot) and 'theorem' (topological-charge-quantization), while their claims are NOT Lean-provable at this abstraction (the docstrings admit this — the geometric content needs the q-torsion leaf / Reeb-derivation substrate). A proposition/theorem block whose Lean only NAMES the claim will read as a proof-statement-integrity gap on the next qa-sweep.

Recommended: demote both blocks to 'conjecture' (kind conjecture, label conj:… , or §3b-cond conditional class if the geometric setup can be packaged as hypotheses and the claim derived). Only external label refs are in the auto-generated definition-index.md. Requires folio-assistant set up (setup-folio-assistant.sh) to run validate + qa-sweep + rebuild the index. Also refresh the 4 q407 content-block sidecars (left stale for theorem→def) once qa-sweep can run.

Blocks: content/quantum-observable-universe/brings-surface/defect-legendrian-knot.{ts,md,lean}; content/quantum-observable-universe/brings-surface/topological-charge-quantization.{ts,md,lean}. Parent: qou-q407.
