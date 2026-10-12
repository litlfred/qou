---
# qou-gzsp
title: '#7673 assembly: Jimbo side as a continuous family + the KZ≅Jimbo comparison theorem with gaps as explicit hypotheses'
status: in-progress
type: task
priority: normal
created_at: 2026-10-12T18:31:38Z
updated_at: 2026-10-12T19:08:37Z
parent: qou-xhci
---

## 2026-10-12 — coordinator re-check: KZ ≅ Jimbo unconditional on the real ray (PR #7744, head a43dcba08a)
lean -DautoImplicit=false -s 65536 QOU/Mass/KohnoAssembly.lean exit 0 (18.9 s, against the prover's rebuilt 134-module cone); #print axioms kz_conj_jimbo_pin, kz_conj_jimbo_hecke = [propext, Classical.choice, Quot.sound]. Non-vacuity checked: the final statement names kzBraidRep (Mass/KZHolonomy/BraidRep.lean) and strandBraid (IwahoriHecke/TensorEmbedding.lean) directly; no local redefinition. Convention: q = e^{2πiκ} in Lean vs e^{iπλ} in the audit doc (λ = 2κ). Not covered: q < 1 (same proof), complex q off the real ray, explicit U, V ≠ ℂ², jimboRep = JimboActionKernel.jimbo (stale cache). Kept in-progress until the q<1 extension or owner sign-off.
