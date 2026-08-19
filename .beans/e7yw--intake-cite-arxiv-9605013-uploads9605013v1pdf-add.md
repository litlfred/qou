---
# e7yw
title: 'Intake + cite: arXiv 9605013 (library/arxiv-nucl-th-9605013v1/9605013v1.pdf) — add to references.ts'
status: completed
type: task
priority: normal
created_at: 2026-07-06T04:46:39Z
updated_at: 2026-07-06T11:21:41Z
parent: 4lss
---

User uploaded library/arxiv-nucl-th-9605013v1/9605013v1.pdf (commit 1804cf09) — a q-deformation nuclear-structure paper. NOT on this branch tree (uploaded on sibling upload branch). Deliverable: confirm arXiv id (likely nucl-th/9605013), add CSL-JSON ref() to content/schema/references.ts, use as bib anchor for the beans above. Route via local/document-intake for a full intake if wanted.

Confirmed arXiv ids from web search (PDFs firewalled in sandbox, proxy 403): NUCLEAR application = nucl-th/9709034 (Raychev, Roussev, Lo Iudice, Terziev, 1997, '3D q-deformed HO applied to the nuclear shell model'); CLUSTER = Bonatsos et al., Chem. Phys. Lett. / quant-ph/9909002 ('3D q-deformed HO and magic numbers of alkali metal clusters'). Uploaded library/arxiv-nucl-th-9605013v1/9605013v1.pdf is likely an earlier related Bonatsos/Raychev q-HO paper — CONFIRM exact id+title from the PDF when accessible. Add CSL-JSON ref() entries for nucl-th/9709034 (+ cluster paper) to content/schema/references.ts. Note q₀=1.10998 => tau=ln q₀=0.1043 for the fixed-q vs fitted-tau comparison.

CORRECTION 2026-07-06 (read the PDF locally, extracted from commit 1804cf09): library/arxiv-nucl-th-9605013v1/9605013v1.pdf IS = Minkov, Drenska, Raychev, Roussev, Bonatsos, 'Nuclear beta- and gamma- collective bands in the SU_q(2) rotator model', nucl-th/9605013, Int. J. Mod. Phys. E (1997). It is the SU_q(2) q-ROTOR paper (bean alyr topic), NOT a q-HO/spin-orbit/magic-number paper. Key facts extracted: H=(1/2θ)C_2[SU_q(2)]+E_0; E_I=(1/2θ)[I][I+1]+E_0 (eq.2); q=e^{iτ} is a PHASE (|q|=1, τ real) => [I]=sin(τI)/sin(τ) (eq.4) — DISTINCT from QOU real q₀>1. τ FITTED per band (Gauss-Newton), τ~0.03-0.07; τ=√3(8N²+22N−15)^{−1/2} ties τ to valence pair number N (eq.7); τ ↔ VMI softness = nuclear stretching. SU_q(2) is a one-band model; unified/magic needs SU_q(3)⊃SO_q(3) (flagged hard). Add CSL ref id minkov1997 (nucl-th/9605013). The q-HO nuclear paper (nucl-th/9709034) is a DIFFERENT, still-unread paper.

READ ALL SIX candidate uploads (2026-07-06, local Read tool). RESULT: 5/6 are OFF-TOPIC for the Elliott/q-def nuclear session — my arXiv-id guess was wrong. Per-paper: (1) 9909088 = Franecki-Kapranov 'Gauss map & noncompact Riemann-Roch for constructible sheaves on semiabelian varieties' (math.AG) — NOT nuclear, but RELEVANT to QOU's homological route: perverse sheaf => Euler char χ≥0, the positivity underlying homological-shell-condensation/BB-stratification. (2) 9911033 = Zhiqin Lu, Bergman-kernel lower bounds on Riemann surfaces (math.DG) — off-topic. (3) 9806163 = Orellana 'Weights of Markov Traces on Hecke Algebras' type B_n/D_n (math.CO) — NOT nuclear, but RELEVANT to QOU tr_M/Wedderburn/Frobenius-pairing: type-B/D Markov-trace weight formula W_{(α,β)}(q,Q), q generic (not root of unity). (4) 9506138 = Lowe-Polchinski-Susskind-Thorlacius-Uglum 'BH Complementarity vs Locality' (hep-th) — off-topic. (5) 9306069 = Susskind-Thorlacius-Uglum 'Stretched Horizon & BH Complementarity' (hep-th) — off-topic. (6) 9308100 = Susskind-Thorlacius 'Gedanken Experiments Involving Black Holes' (hep-th) — off-topic. CONCLUSION: the actual Elliott/Kibler/SU_q(2)-screening source papers are NOT in this batch; only confirmed on-topic upload remains 9605013 (SU_q(2) rotor). Two math papers (9806163 Markov-B/D, 9909088 perverse-sheaf positivity) are worth separate QOU-substrate follow-up, unrelated to this session's nuclear topic.

## Resolution (2026-07-11)

Core deliverable satisfied. The CSL-JSON reference for the paper
(Minkov-Drenska-Raychev-Roussev-Bonatsos, "Nuclear beta- and gamma- collective
bands in the SU_q(2) rotator model", nucl-th/9605013) already exists in
`content/schema/references.ts` as id **`minkov1996`** and is cited from
`observations/q-deformed-nuclear-models-comparison.md` §"SU_q(2) rotor bands"
— so the intake+cite goal (add ref + use as bib anchor) is met (ref id is
`minkov1996`, not the tentatively-proposed `minkov1997`). Two math papers noted
in the body worth a SEPARATE future QOU-substrate follow-up, unrelated to this
nuclear session (left open, not part of this bean): 9806163 (Orellana, Markov
traces on type B/D Hecke — relevant to tr_M/Wedderburn) and 9909088
(Franecki-Kapranov perverse-sheaf positivity — relevant to the homological
shell-condensation route). A full document-intake of the PDF (vs. the cite) was
optional per the original body and is not blocking.
