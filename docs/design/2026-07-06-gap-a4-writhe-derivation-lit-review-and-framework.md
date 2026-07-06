# GAP-A-4 [1⁴] exchange writhe — literature anchor + derivation framework

**Date:** 2026-07-06 · **Discipline:** formalize-first / no-fit (AGENTS.md). Research
note for the one open object in the ⁴He magnitude arc: the **writhe structure that
fixes the sign-carrying exchange matrix `G`** in the pinned value form
`b₄ = −ln det(I + G)` (Perron–Frobenius forced `G` sign-carrying; the two naive
principled exchanges failed, `b4_antisym_hecke_exchange_derivation`).

## 1. Literature anchor — the α binding IS the Wigner SU(4) supermultiplet energy

The whole [1⁴] approach is **externally validated** by established nuclear physics:

- The spin-isospin degrees of freedom of A nucleons are described by **SU(4), the
  Wigner supermultiplet group**; the anomalously large binding of even-even N=Z
  nuclei is *"a consequence of Wigner's SU(4) symmetry"* (the [1⁴] closed shell at
  the α). Refs: Wigner SU(4) & ¹²C clustering ([arXiv:2106.04834](https://arxiv.org/pdf/2106.04834));
  SU(4) branching rules ([arXiv:2511.00216](https://arxiv.org/html/2511.00216v1)).
- Standard mass models carry a phenomenological **Wigner term**
  `E_W = W(A)·|N−Z|/A` (coefficient `a_W ≈ 47 MeV` traditional; origin
  [nucl-th/9702054](https://arxiv.org/abs/nucl-th/9702054); physical origin,
  ScienceDirect S0370269398004584). **Key point:** the `|N−Z|` term *vanishes at
  N=Z*, so the α's extra binding is the **SU(4) closed-shell exchange energy the
  models add by hand** — exactly the connected `b₄ = 9.243 MeV` the framework aims
  to derive.

**Consequence.** The framework's `b₄` is the *microscopic derivation of the Wigner
supermultiplet closed-shell binding* — a quantity nuclear physics treats
phenomenologically. This is a strong motivation and a hard cross-check target
(the α SU(4) closed-shell energy), and it confirms the value is real and ≥4-body,
matching the I-conn / gate results.

## 2. No precedent for the braid-writhe leg — it is novel

The Hecke/Markov/writhe literature is **pure knot theory** — Jones' Markov trace
on Iwahori–Hecke algebras, braids-and-ties, weaving-knot trace algorithms
([arXiv:math/0405508](https://arxiv.org/pdf/math/0405508),
[arXiv:1908.04152](https://arxiv.org/pdf/1908.04152)). **None** connects a
*nucleon-braid exchange writhe* to *binding*. So the QOU-specific derivation —
nucleons as 3-quark braids, their [1⁴] antisymmetric exchange as a physical
crossing whose sign is the writhe — has no external template and must be built
in-house. (This is expected: the braid-nucleon model is the framework's own.)

## 3. Derivation framework (the object to build)

`G_{ij}` = the exchange amplitude between nucleon-braids `i, j` in the [1⁴] shell.
Physically the exchange is a **crossing** of two 3-quark blocks; the amplitude is a
**writhe-signed Hecke crossing weight**:

    G_{ij} = (−q^{-1/2})^{w_{ij}} · (normalisation),

where `w_{ij}` is the **writhe** (signed crossing number) of exchanging blocks
`i` and `j` in the ⁴He [1⁴] link closure, and `−q^{-1/2}` is the antisymmetric
Hecke eigenvalue (the derived sign source). The connected `b₄ = −ln det(I+G)` is
then the Wigner supermultiplet exchange energy of §1.

**What the naive attempts taught us** (`b4_antisym_hecke_exchange_derivation`):
- uniform `w=1` (`G_{ij}=λ_−·z=−0.474`) → det<0, unphysical (over-rotates);
- `G_{ij}=−h/2` → 28× too small.
So the **per-pair writhe `w_{ij}` is non-trivial and non-uniform** — the like-pair
(pp/nn) and unlike-pair (pn) exchanges have different crossing structure, and the
magnitude must land `G`'s dominant eigenvalue in `(−1, 0)` (so `1+λ_dom>0`,
det>0) while summing to `b₄=9.24`.

## 4. Concrete next step (the open derivation — NOT a fit)

Build the **⁴He [1⁴] link diagram** explicitly: 4 nucleon-blocks (3 strands each),
antisymmetrically closed, and read off the per-pair writhe `w_{ij}` from the actual
crossings (over/under from the framing convention). Then `G_{ij}` is *determined*
(no free parameter), and `−ln det(I+G)` is a *prediction* checked against 9.243 —
a verdict, never a fit. The pp/nn vs pn writhe asymmetry is the p↔n (bar-odd)
structure already seen in I-par.

Prereqs / reuse: the framework's link-closure + writhe tooling (`_li_2_q_util`,
`aj_*` colored-Jones towers), the nucleon braid words (`mass_at_3A_proper`), and
the framing convention (`snappy_*` cusp seeding). This is a dedicated derivation
unit, not a session-tail probe.

### 4a. Structural finding — the committed word is a CHAIN, not the [1⁴] complete graph

Inspection of `mass_at_3A_proper.atom_braid_word_3A(2,2)` (its own docstring):
the ⁴He word is an **intra pass** per nucleon (the 3-quark block) plus a single
**inter pass at generator `3k+2`** between *adjacent* nucleons — a **linear
chain** with only **3 inter-crossings** (nucleon 1–2, 2–3, 3–4), NOT the
`C(4,2)=6`-pair **[1⁴] complete graph** the closed shell requires. This is
precisely why `B_sym`, built on this chain word, under-binds ⁴He (11.97 vs 28.30):
it carries no antisymmetric [1⁴] closure and half the pair-crossings.

**Consequence for the derivation.** The [1⁴] exchange matrix `G` is a genuinely
NEW link diagram — the antisymmetric complete-graph closure of the 4 nucleon
blocks — not extractable from the committed chain word. The open piece is the
**per-pair writhe SIGN** `sgn(w_{ij})` (over/under of each of the 6 block
crossings), set by the [1⁴] framing/orientation. Uniform same-sign `w=1` failed
(det<0); a **mixed-sign** pattern (pp/nn vs pn — the p↔n bar-odd structure of
I-par) is what can put `G`'s dominant eigenvalue in `(−1,0)`. Fixing those signs
from the explicit [1⁴] framing is the remaining derivation — and must be read off
the diagram, never chosen to hit 9.243.

## 5. Sources

- [arXiv:2106.04834](https://arxiv.org/pdf/2106.04834) — Wigner SU(4), clustering, ¹²C.
- [arXiv:2511.00216](https://arxiv.org/html/2511.00216v1) — SU(4) spin-isospin branching rules.
- [nucl-th/9702054](https://arxiv.org/abs/nucl-th/9702054) — origin of the Wigner energy.
- ScienceDirect S0370269398004584 — physical origin of the Wigner term.
- [arXiv:math/0405508](https://arxiv.org/pdf/math/0405508) — Markov traces / Hecke type B.
- [arXiv:1908.04152](https://arxiv.org/pdf/1908.04152) — Hecke trace algorithm, weaving knots.
