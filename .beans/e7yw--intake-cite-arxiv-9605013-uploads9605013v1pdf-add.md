---
# e7yw
title: 'Intake + cite: arXiv 9605013 (uploads/9605013v1.pdf) — add to references.ts'
status: todo
type: task
priority: normal
created_at: 2026-07-06T04:46:39Z
updated_at: 2026-07-06T11:15:26Z
parent: 4lss
---

User uploaded uploads/9605013v1.pdf (commit 1804cf09) — a q-deformation nuclear-structure paper. NOT on this branch tree (uploaded on sibling upload branch). Deliverable: confirm arXiv id (likely nucl-th/9605013), add CSL-JSON ref() to content/schema/references.ts, use as bib anchor for the beans above. Route via local/document-intake for a full intake if wanted.

Confirmed arXiv ids from web search (PDFs firewalled in sandbox, proxy 403): NUCLEAR application = nucl-th/9709034 (Raychev, Roussev, Lo Iudice, Terziev, 1997, '3D q-deformed HO applied to the nuclear shell model'); CLUSTER = Bonatsos et al., Chem. Phys. Lett. / quant-ph/9909002 ('3D q-deformed HO and magic numbers of alkali metal clusters'). Uploaded uploads/9605013v1.pdf is likely an earlier related Bonatsos/Raychev q-HO paper — CONFIRM exact id+title from the PDF when accessible. Add CSL-JSON ref() entries for nucl-th/9709034 (+ cluster paper) to content/schema/references.ts. Note q0=1.10998 => tau=ln q0=0.1043 for the fixed-q vs fitted-tau comparison.

CORRECTION 2026-07-06 (read the PDF locally, extracted from commit 1804cf09): uploads/9605013v1.pdf IS = Minkov, Drenska, Raychev, Roussev, Bonatsos, 'Nuclear beta- and gamma- collective bands in the SU_q(2) rotator model', nucl-th/9605013, Int. J. Mod. Phys. E (1997). It is the SU_q(2) q-ROTOR paper (bean alyr topic), NOT a q-HO/spin-orbit/magic-number paper. Key facts extracted: H=(1/2θ)C_2[SU_q(2)]+E_0; E_I=(1/2θ)[I][I+1]+E_0 (eq.2); q=e^{iτ} is a PHASE (|q|=1, τ real) => [I]=sin(τI)/sin(τ) (eq.4) — DISTINCT from QOU real q0>1. τ FITTED per band (Gauss-Newton), τ~0.03-0.07; τ=√3(8N²+22N−15)^{−1/2} ties τ to valence pair number N (eq.7); τ ↔ VMI softness = nuclear stretching. SU_q(2) is a one-band model; unified/magic needs SU_q(3)⊃SO_q(3) (flagged hard). Add CSL ref id minkov1997 (nucl-th/9605013). The q-HO nuclear paper (nucl-th/9709034) is a DIFFERENT, still-unread paper.
