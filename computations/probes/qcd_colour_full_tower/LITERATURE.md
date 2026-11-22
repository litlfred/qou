# LITERATURE: colour, Markov traces and β₀ (beans `qou-ni4b`, `qou-bwwr`; PR #9059)

Owner's question (verbatim): *"What does the literature say? Any guidance there? Do we need more papers?"*

This is a literature survey only. It adds no code and no new compute. It covers the three results
from this PR:

1. **Colour action** (`qcd_colour_action/`, `qcd_spin_factor/`). A strand-wise colour action that
   commutes with the Hecke crossing and moves with the strand forces q² = 1. Adding spin does not
   help at real q > 1, within the enumerated class.
2. **Colour in the tower** (`qcd_colour_full_tower/`). On (ℂ³)^⊗n with Jimbo U_q(gl₃), a diagonal
   twist of rank 1, 2 or 3 gives z = q, z_D = q³/(q²+1) or q³/[3]_q. Only the rank-3 twist is
   U_q(gl₃)-invariant. Convention D's radical holds the three-row blocks, so every colour singlet
   (A,A,A) is invisible to D. D's residual symmetry is U_q(gl₂) × U(1).
3. **Scale and β₀** (`qcd_heat_kernel/`, `qcd_scale_candidates/`, `qcd_spin_background/`). No
   scale variable gave antiscreening together with logarithmic running. The Ocneanu isotypic weight
   gives b = N/(k+N) > 0, but as a power law. No Nielsen–Hughes (2s)² − 1/3 split appeared.

Search date 2026-11-22. Every URL below came back from a web search in this session. **Verified**
means the title and abstract were read (by fetching the abstract, or from the held text in
`library/`). **Located** means only the search result's title and URL were seen.

---

## Verdict (headline)

**Result 2 is mostly already in the literature. Our probe rederives it; it is not a new theorem.**
Its parts:

- *A Markov trace on H_n(q) comes from a twisted ("enhanced") quantum trace Sp(b(β)∘μ^⊗n) on
  V^⊗n.* This is **Turaev 1988** (held: `turaev1988`). His enhanced Yang–Baxter operator μ is
  exactly our diagonal twist K. HOMFLY comes from gl_N, with N the dimension of V.
- *The Markov parameter is set by how many rows the trace can see, and the k-row trace is the
  SU(k)/U_q(gl_k) trace. It kills every Young diagram with more than k rows.* This is **Wenzl 1988**
  (held: `wenzl1988`; its text has "all Young diagrams with at most k rows" and "representation of
  SU(k) corresponding to λ"), building on **Ocneanu** and **Jones 1987**. The Jones trace (our
  convention D) is the k = 2 case, i.e. the Temperley–Lieb quotient, whose radical is the diagrams
  with ≥ 3 rows. That is the statement "every three-row block, so every (A,A,A) singlet, has D-weight
  0". The repo already holds it as the Lean lemma
  `ocneanuWeight_conventionD_eq_zero_of_three_rows`.
- *A rank-r twist on ℂ^N gives the gl_r trace.* This is elementary: K^⊗n kills every basis tensor
  with an index outside supp K, so the twisted trace on (ℂ^N)^⊗n equals the twisted trace on
  (ℂ^r)^⊗n. The stabiliser of a rank-2 projection in gl₃ is the Levi subalgebra gl₂ ⊕ gl₁. The
  survey found no paper that states this as a separate result. It is a one-line corollary of
  Turaev plus Wenzl.

**What may be new in result 2 is only the physical reading.** That reading is: "the Jones/D trace is
the SU(3) colour trace with one colour switched off, so it breaks colour to U(2) × U(1) and every
colour singlet lies in its radical." No preon or braid-matter paper found here uses Markov traces
or Hecke quotients at generic q at all (see §C). So the *reading* has no precedent in what was
searched, while the *mathematics* has a 1988 citation. **Recommendation (judgement, not finding):**
cite Turaev 1988 and Wenzl 1988 as the source of result 2. Describe the probe as an explicit check
of them on (ℂ³)^⊗n, and keep the colour reading as the repo's own interpretation.

**Result 1 (q² = 1) has no direct statement in what was searched.** It is consistent with the
general pattern below and with Schur–Weyl (Jimbo 1986): the commutant of the Hecke action on
(ℂ^N)^⊗n is U_q(gl_N) itself. An extra strand-wise colour factor would therefore have to sit inside
that commutant (colour fixed in position) or be a classical symmetric-group factor (q = 1). Treat
our Gröbner result as a corollary-shaped rederivation inside a named class, not as new.

**Result 3 (β₀) has no precedent in the knot / quantum-group literature that was found.** The one
known "level shift" fact, that Chern–Simons quantities run with k → k + N, has the same shape as our
N/(k+N), but it is a one-loop shift of a topological coupling, not running with energy. Our power
law matches that literature's structure, and it confirms rather than closes the gap.

---

## What the repo already holds (corpus-grep path 5)

`library/INDEX.md` (806 directories) plus a `sections/` and `ocr/` grep. `bun scripts/corpus-search.ts`
was run from `/home/claude/qou`; the worktree copy fails because `folio-assistant` is not linked
there. "helon" gave 10 ingested seeds, 0 authored. "Markov trace" gave 38 ingested seeds plus
authored hits. `emptyRoots` was empty in both.

| doc-id | work | bears on |
|---|---|---|
| `turaev1988` | Turaev, *The Yang–Baxter equation and invariants of links*, Invent. Math. 92 (1988) | **R2 core.** Enhanced YB operator = twisted operator trace on V^⊗n; HOMFLY from gl_N |
| `wenzl1988` | Wenzl, *Hecke algebras of type A_n and subfactors*, Invent. Math. 92 (1988) | **R2 core.** k-row quotients ↔ SU(k); Ocneanu trace weights |
| `reshetikhin-turaev` | Reshetikhin–Turaev, *Ribbon graphs and their invariants derived from quantum groups* | R2: the quantum trace is the pivotal (rank-N) twist |
| `arxiv-0911.4494v2` | *The geometry of Markov traces* (Jones–Ocneanu trace via equivariant cohomology) | R2 background |
| `arxiv-2507.19896v1` | *Generalized Markov traces and Jucys–Murphy elements* | R2/R3: JM-weighted traces (the N2 arm) |
| `arxiv-1403.4021v2` | *Markov traces on the BMW algebras* | spin/orthogonal analogue |
| `erlijman-wenzl-pjm-231-2` | Erlijman–Wenzl, *Subfactors from braided C* tensor categories* | R2: index ↔ rank |
| `ram1991-frobenius-formula`, `hecke-alg`, `hdr`, `black-samson-phd2010sp` | Hecke characters, Schur algebras | R2 machinery |
| `rosso-1988-cmp-117-581`, `du-1995-algebra-colloq-2-363` | U_q(g) reps; quantised Weyl reciprocity | R1/R2: Jimbo–Schur–Weyl |
| `arxiv-1712.08953v1` | *Representations of the oriented skein category* | HOMFLY ↔ gl_N interpolation |
| `arxiv-hep-ph-0503213v2` | Bilson-Thompson, *A topological model of composite preons* (helon) | **R1/R3 physics** |
| `0603022v2` | Bilson-Thompson–Markopoulou–Smolin, *Quantum gravity and the standard model* | R1 physics |
| `arxiv-1901.01312v1` | Gresnigt, *Braided fermions from Hurwitz algebras* | R1 physics |
| `arxiv-2106.01332v4` | *Braided matter interactions … via 1-handle attachment* | R1 physics |
| `arxiv-2306.13098v2`, `eps-hep2019-615` | Gresnigt et al., sedenion generations with colour | R1 physics |
| `furey-2018-epjc-78-375` | Furey, *SU(3)_C × SU(2)_L × U(1)_Y (× U(1)_X) as a symmetry of division algebraic ladder operators* | R1/R2 physics |
| `arxiv-1910.09966v1` | *Braids, 3-manifolds, elementary particles* | R1 physics |
| `arxiv-0806.3105v3` | Finkelstein, *Knots and preons* (SL_q(2) trefoils) | R1: q-deformed but SU(2)-only |

**Not held, and the index has no hits for them:** Jimbo 1986; Jones 1987 (Annals); HOMFLY-PT 1985;
any level–rank duality paper; any quantum-symmetric-pair / coideal paper (the `sections/` hits for
"coideal" are Hopf-algebra uses, not Letzter–Kolb); Gresnigt 2018 *Braids, normed division
algebras…*; Gresnigt 2017 *Quantum groups and braid groups as fundamental symmetries*;
Chester–Arsiwalla–Kauffman 2025; Nielsen/Hughes on asymptotic freedom.

---

## A. Markov traces from twisted quantum traces; z ↔ rank

| paper | status | one line | bears on |
|---|---|---|---|
| Jones, *Hecke algebra representations of braid groups and link polynomials*, Ann. Math. 126 (1987) — <https://annals.math.princeton.edu/1987/126-2/p05> | located (classic) | Ocneanu trace on H_∞(q); two-variable polynomial; Jones = TL quotient | **confirms R2** (TL quotient = ≤ 2 rows) |
| Freyd–Yetter–Hoste–Lickorish–Millett–Ocneanu, *A new polynomial invariant of knots and links*, BAMS 12 (1985) — <https://www.doi.org/10.1090/S0273-0979-1985-15361-3> | located | HOMFLY(-PT) | context |
| Jimbo, *A q-analogue of U(gl(N+1)), Hecke algebra, and the Yang–Baxter equation*, LMP 11 (1986) — <https://www.doi.org/10.1007/BF00400222> | located | quantum Schur–Weyl duality: U_q(gl_N) and H_n(q) are mutual commutants on (ℂ^N)^⊗n | **confirms R1/R2 setting**; the commutant structure is why colour-fixed-or-q=1 is forced |
| Turaev 1988 — held `turaev1988` | verified (held text) | Sp(b(β)∘μ^⊗n), μ = enhancement = twist | **confirms R2** directly |
| Wenzl 1988 — held `wenzl1988`; <https://eudml.org/doc/143571> | verified (held text) | quotients by Young diagrams with ≤ k rows ↔ SU(k); Ocneanu weights | **confirms R2**; D = k = 2 |
| *The geometry of Markov traces* — <https://arxiv.org/pdf/0911.4494> (held) | verified (index) | geometric Jones–Ocneanu trace | background |
| *Generalized Markov traces and Jucys–Murphy elements* — <https://arxiv.org/pdf/2507.19896> (held) | verified (index) | Markov traces built from JM elements | R3 N2 arm: the JM-weighted family is a known generalisation |

## B. Level–rank duality and SU(2) vs SU(3)

| paper | status | one line | bears on |
|---|---|---|---|
| Naculich–Schnitzer, *Level-rank duality of the U(N) WZW model, Chern–Simons theory, and 2d qYM theory*, hep-th/0703089 — <https://arxiv.org/abs/hep-th/0703089> | verified (abstract) | U(N)_K ↔ U(K)_N dualities at q = e^{2πi/(N+K)} | context only. Level–rank needs a root of unity; it says nothing at real q₀ > 1 |
| Naculich–Schnitzer (et al.), hep-th/9205082 — <https://arxiv.org/abs/hep-th/9205082> | located | earlier SU(N)_K level–rank for knot invariants | same |

**Guidance on "why a colour-invariant trace cannot be the Jones trace".** No paper found states it in
those words, because it is immediate from §A. A Markov trace is fixed by z (Ocneanu). The
U_q(gl₃)-invariant (pivotal) trace on ℂ³ has the 3-row value q³/[3]_q, and the Jones value is the
2-row one, so they differ. Level–rank duality is a red herring at generic real q.

## C. Standard-Model particles from braids: how each gets colour

| paper | status | how colour enters | generic q? | moves with strand? |
|---|---|---|---|---|
| Bilson-Thompson, *A topological model of composite preons*, hep-ph/0503213 — <https://arxiv.org/abs/hep-ph/0503213> (held) | verified | colour = which of the three ribbons carries the twist (permutation of twists) | **no**, classical B₃ with framing | as a permutation label, at q = 1 |
| Bilson-Thompson–Markopoulou–Smolin, *Quantum gravity and the standard model*, hep-th/0603022 — <https://arxiv.org/abs/hep-th/0603022> (held) | verified (search + held) | same, embedded in braided spin networks | no | no |
| *Embedding the Bilson-Thompson model in an LQG-like framework*, arXiv:1002.1462 — <https://arxiv.org/pdf/1002.1462> | located | same | no | — |
| Gresnigt, *Braids, normed division algebras, and Standard Model symmetries*, arXiv:1803.02202 — <https://arxiv.org/abs/1803.02202v2> | verified (abstract) | identifies helon braids with Furey's minimal ideals of ℂ⊗𝕆; SU(3)_c is **inherited from the octonions**, not from braiding | **no**, classical B₂, B₃^c | — |
| Gresnigt, *Braided fermions from Hurwitz algebras*, arXiv:1901.01312 (held) | verified (index) | same programme | no | — |
| Gresnigt, *A topological model of composite preons from the minimal ideals of two Clifford algebras*, arXiv:2004.11140 — <https://arxiv.org/pdf/2004.11140v2> | located | Cℓ(6) ideals × braids | no (by title/abstract snippet) | — |
| Gresnigt, *Quantum groups and braid groups as fundamental symmetries*, arXiv:1711.09011 — <https://arxiv.org/pdf/1711.09011> | verified (fetched) | SU_q(3) used as a **flavour** symmetry (baryon masses); colour comes from the helon twists or the octonions | q appears only in the flavour sector | — |
| Furey, *Generations: three prints, in colour*, arXiv:1405.4601 — <https://arxiv.org/pdf/1405.4601>; *Charge quantization from a number operator*, arXiv:1603.04078 — <https://arxiv.org/pdf/1603.04078>; EPJC 78 (2018) 375 (held `furey-2018-epjc-78-375`) | located / held | SU(3)_c as the automorphisms of ℂ⊗𝕆 fixing a unit; ladder operators | no q | no strands |
| Chester–Arsiwalla–Kauffman, *Preons, braid topology, and representations of fundamental particles*, arXiv:2501.03260 — <https://arxiv.org/pdf/2501.03260> | verified (fetched) | helon states mapped to A₂ weight lattice; argue helons capture only SU(3)_c × U(1)_em | **no**, classical B₃ → SL(2,ℤ) | — |
| Kauffman–Lomonaco, braiding and topological quantum computing, quant-ph/0606114 — <https://arxiv.org/pdf/quant-ph/0606114>; arXiv:0707.3678 — <https://www.arxiv.org/pdf/0707.3678> | located | Fibonacci/TL anyon braiding; no SM colour | root of unity | — |
| Finkelstein, *An SL_q(2) extension of the Standard Model*, arXiv:1205.1026 — <https://arxiv.org/pdf/1205.1026>; *Knots and preons* (held `arxiv-0806.3105v3`) | verified (fetched) | q-deformation is **SU(2)/knot only**; colour is postulated on preons | generic q, but colour is not q-deformed | no |

**Finding (absence-of-evidence, stated as such).** In every braid-matter programme found, SU(3) colour
either (i) is a classical permutation label on ribbons at q = 1 (Bilson-Thompson, Chester–Arsiwalla–
Kauffman), or (ii) comes from a division algebra and is attached to braid states by identification
(Gresnigt, Furey), or (iii) is postulated (Finkelstein). **None has colour moving with the strand
under a Hecke braiding at generic q.** That pattern agrees with our result 1 (q² = 1 forced) and does
not contradict it. Searched surface: the papers above plus the held `sections/`. A paper we did not
find could still exist.

## D. gl₃ → gl₂ × gl₁ and electroweak structure in preon/braid models

No braid or preon paper found derives an electroweak U(2) from switching off one colour. The closest
links:

- Finkelstein's SL_q(2) model puts the q-deformation on the **SU(2)** side
  (<https://arxiv.org/pdf/1205.1026>, <https://arxiv.org/pdf/1511.07919>).
- Pati–Salam-type "lepton as fourth colour" ideas break colour as SU(4) → SU(3) × U(1)
  (*Advantages of unity with SU(4)-color*, held `arxiv-1706.09531v1`). The pattern is the same
  Levi-branching shape, but the group is SU(4), not SU(3).
- Gresnigt's sedenion papers (held) and Furey (held) get SU(2)_L × U(1) from the division-algebra
  structure, not from a rank-2 projection inside gl₃.

So the reading "D's residual U_q(gl₂) × U(1) is electroweak-like" has **no precedent in what was
searched**. It needs a derivation of its own and must not be presented as an identification.
(Per AGENTS.md "Defined residual ≠ derived decomposition": a symmetry-group coincidence is not an
identification.)

## E. Asymptotic freedom / β-functions from quantum groups or knots

| paper | status | bears on |
|---|---|---|
| Nielsen, *Asymptotic freedom as a spin effect*, Am. J. Phys. 49 (1981); Hughes (1980/81) — discussed in Baez, *This Week's Finds* 94 — <https://math.ucr.edu/home/baez/week94.html> | located (secondary) | the (2s)² − 1/3 paramagnetic/diamagnetic split we looked for and did not find (R3) |
| Wilczek, *Twenty-five years of asymptotic freedom*, hep-th/9809060 — <https://arxiv.org/pdf/hep-th/9809060> | located | standard reference for the spin picture |
| *Asymptotic freedom from thermal and vacuum magnetization*, hep-ph/9601259 — <https://arxiv.org/pdf/hep-ph/9601259> | located | magnetisation picture of b₀ |
| Chern–Simons regularisation and the k → k + N shift, e.g. *Regularization and renormalization of Chern–Simons theory*, hep-th/9210113 — <https://arxiv.org/pdf/hep-th/9210113> | located | **same shape as our b = N/(k+N)**: the knot-theory "running" is a finite one-loop shift by the dual Coxeter number C_A = N, not a logarithm |

**Finding.** No paper found derives a logarithmic, antiscreening β-function from a quantum group,
Hecke algebra or knot invariant. The only C_A-shaped quantum-group effect in the literature is the
k → k + N shift, which is a power-law/finite effect. That is exactly the shape of our N1 result.
So our N1 "C_A without logs" is the expected outcome, not an anomaly, and R3's MISS agrees with the
literature. Absence of evidence, searched surface as listed.

## F. Coideal subalgebras / quantum symmetric pairs: a route past q² = 1?

| paper | status | one line |
|---|---|---|
| Letzter, *Coideal subalgebras and quantum symmetric pairs*, math/0103228 — <https://arxiv.org/abs/math/0103228> | located | the founding construction: a q-analogue of U(𝔨) ⊂ U(𝔤) for a symmetric pair, as a coideal (not Hopf) subalgebra |
| Balagović–Kolb, *Universal K-matrix for quantum symmetric pairs*, arXiv:1507.06276 — <https://arxiv.org/pdf/1507.06276> | verified (abstract) | K-matrix commuting with the coideal; reflection equation; braids in a cylinder (type B) |
| Kolb–Stokman, *Reflection equation algebras, coideal subalgebras and their centres*, (search hit) math/0512581 — <https://arxiv.org/pdf/math/0512581> | located | reflection equation ↔ coideals |
| *Comparison of quantizations of symmetric spaces: cyclotomic KZ and Letzter–Kolb coideals*, arXiv:2009.06018 — <https://arxiv.org/pdf/2009.06018> | located | KZ side of the same objects (relevant to the K1–K3 KZ arms) |

**Guidance (judgement).** This is the one mathematically sound route that the literature offers past
result 1. A coideal subalgebra B ⊂ U_q(gl₃) is **not** a Hopf subalgebra, so it does not have to act
diagonally on V^⊗n "strand-wise and commuting with Ř" in the sense our class assumed. Its natural
braid partner is the **type-B / cylinder braid group** with a K-matrix at one end, not the type-A
Hecke algebra. This matches AGENTS.md §7b (type-B folding). Two cautions. (i) It changes the algebra
(type A → type B, Hecke → two-parameter Hecke / reflection equation), so it is a new model, not a
loophole in the old one. (ii) The fixed-point subalgebras of a symmetric pair for gl₃ are so₃ or
gl₂ ⊕ gl₁, which is **smaller** than gl₃. So a coideal colour would itself be broken colour, as in
result 2. No paper found builds SU(3) colour this way.

---

## Do we need more papers? Ranked acquisitions (judgement)

| # | paper | URL | why |
|---|---|---|---|
| 1 | Jones 1987, Annals 126 | <https://annals.math.princeton.edu/1987/126-2/p05> | primary citation for result 2 (Ocneanu trace, TL = 2-row quotient); not held |
| 2 | Jimbo 1986, LMP 11 | <https://www.doi.org/10.1007/BF00400222> | primary citation for the U_q(gl_N)–H_n(q) commutant underlying results 1 and 2; not held |
| 3 | Gresnigt 2018, *Braids, normed division algebras, and SM symmetries* | <https://arxiv.org/abs/1803.02202v2> | the closest braid↔colour bridge; result 1 should be checked against it |
| 4 | Letzter 2001, *Coideal subalgebras and quantum symmetric pairs* | <https://arxiv.org/abs/math/0103228> | the only route past q² = 1 the literature offers |
| 5 | Balagović–Kolb 2015, *Universal K-matrix for QSP* | <https://arxiv.org/pdf/1507.06276> | the braid (cylinder) side of #4 |
| 6 | Chester–Arsiwalla–Kauffman 2025, *Preons, braid topology…* | <https://arxiv.org/pdf/2501.03260> | most recent survey of how braid models get SU(3)_c; argues helons give only SU(3)_c × U(1)_em |
| 7 | Gresnigt 2017, *Quantum groups and braid groups as fundamental symmetries* | <https://arxiv.org/pdf/1711.09011> | only paper found that puts U_q(su₃) and braids side by side (for flavour) |
| 8 | Freyd et al. 1985 (HOMFLY) | <https://www.doi.org/10.1090/S0273-0979-1985-15361-3> | completes the HOMFLY ↔ gl_N citation chain |

Items 1, 2 and 8 change what we may *claim* (they make result 2 a citation). Items 3–7 change what
we might *try next*. If acquisition is costly, 1, 2 and 4 are the ones that matter. Item 1's text is
partly duplicated by the held `wenzl1988` and `turaev1988`, so result 2 can already be cited today.

## Key guidance for the next step

1. **Cite, don't claim, result 2.** Turaev 1988 + Wenzl 1988 (both held) plus Jones 1987. The repo's
   addition is the explicit (ℂ³)^⊗n check and the colour-singlet ⊂ radical(D) reading.
2. **Result 1 fits a uniform pattern in the physics literature.** Nobody gets q-deformed colour that
   moves with the strand. If that is the goal, the literature points to changing the algebra
   (coideal / type-B, §F) or to taking colour from outside the braid (division algebras, §C). It
   does not point to a cleverer type-A construction.
3. **Result 3: the literature predicts the MISS.** Quantum-group "running" is the k → k + N shift
   (C_A-shaped, power law). A logarithm needs a genuine continuum/energy integral that the Hecke
   tower does not supply. No precedent for β₀ from Hecke data was found.
4. **Do not read U_q(gl₂) × U(1) as electroweak** without a derivation. No precedent exists, and the
   identification would be selection by shape.

## Method and limits

- Web searches (standard mode), 2026-11-22: 15 queries. Abstracts fetched for 1803.02202,
  2501.03260, 1711.09011, hep-th/0703089, 1507.06276, 1205.1026. Held texts grepped for
  `wenzl1988` and `turaev1988`.
- Not done: full-text reading of Jones 1987, Jimbo 1986 or Letzter 2001, which are not held.
  Statements about them above are standard textbook content, marked **located** rather than
  verified.
- Every "not found" above is a statement about this search surface, not a proof of absence.
