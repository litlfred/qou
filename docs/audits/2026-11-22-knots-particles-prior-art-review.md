# Prior art for the knots-and-particles chapter: braid preons and quantum symmetric pairs

Date: 2026-11-22. Owner request: *"Review these to see what we should add to the prior art on
knots and particles chapter intro"* (five PDFs attached to the agent chat).

## Target block

The chapter `chap:knots-particles-confinement` already has a prior-art block:
[`prose:knotted-particles-history`](../../folio/quantum-observable-universe/knots-particles-confinement/knotted-particles-history.md),
the second block of §1 *Interactions are pairwise* (added in `a948aee0697`). It covers the
vortex-atom lineage (Helmholtz, Kelvin, Maxwell, Tait), its modern descendants (Moffatt, Witten,
Faddeev–Niemi, Kleckner–Irvine, Kedia et al.) and Avrin's twisted-band fermions. Before this
change it cited **none** of the braid-preon programme: no Bilson-Thompson, Gresnigt, Furey,
Finkelstein or Chester–Arsiwalla–Kauffman, although `bilson-thompson2005`,
`bilsonthompson2007`, `gresnigt2019`, `gresnigt2023`, `furey2018`, `finkelstein2008` and
`kauffman-lomonaco-2007` were all registered and cited elsewhere (the Standard-Model appendix).
That gap is the substance of this review.

## What was read

Text read from the ingested `library/<doc-id>/sections/` (see §Ingest) and page 1 of each PDF.

| paper | read |
|---|---|
| Gresnigt 2017 | all sections (10 pp) |
| Chester–Arsiwalla–Kauffman 2025 | front matter, §1, §4 (CPT / $PSL(2,\mathbb{Z})$), §2.2 colour passages, §7 conclusions, Table 2 |
| Gresnigt 2018 | front matter, abstract, §6 discussion; §2–5 headings only |
| Balagović–Kolb 2015 | page 1 (abstract, §1.1), section titles |
| Letzter 2001 | page 1 (abstract), introduction, section titles |
| Finkelstein 2008 (held, `arxiv-0806.3105v3`) | introduction |

## Per paper

### 1. Gresnigt, *Quantum groups and braid groups as fundamental symmetries* (2017)

arXiv:1711.09011v1 [physics.gen-ph]. Page 1 names the venue: EPS-HEP 2017, European Physical
Society Conference on High Energy Physics, 5–12 July 2017, Venice (Proceedings of Science, licence
line pos.sissa.it). The PoS article number is not printed on the arXiv copy. Key `gresnigt2017`.

**Summary.** Two parts. (i) A review of Gavrilik's and Gresnigt's use of $SU_q(3)$ as a *flavour*
symmetry: generalised Gell-Mann–Okubo baryon mass formulas whose best fit to data is at a root of
unity, $q = e^{i\pi/7}$ for the octet and $q = e^{i\pi/21}$ for the decuplet (0.6 % and 0.3 %
errors in its Table 1). (ii) Using the Kauffman–Lomonaco Clifford braiding theorem,
$\sigma_k = (1 + e_{k+1}e_k)/\sqrt{2}$, it shows that $\mathbb{C}$ and $\mathbb{H}$ represent
$B_2$ and the circular braid group $B_3^c$, the two groups of the helon model, whose framed braids
form $B_3^c \ltimes (\tfrac12\mathbb{Z})^3$.

**Colour.** Not from braiding. Helon colour is the permutation of twists; on the algebra side
$SU(3)_c$ comes from Furey's complex octonions.

**q.** Appears only in the flavour quantum group, as a root of unity chosen by fit. The braid
generators are not deformed. (Our observation, not the paper's: the Clifford generators have
order 8 and satisfy the fixed quadratic $\sigma^2 - \sqrt{2}\,\sigma + 1 = 0$, eigenvalues
$e^{\pm i\pi/4}$. That is one specialised Hecke-type relation, not $H_n(q)$ at generic $q$.)

**Relation to the chapter: precedent and contrast.** Precedent for braids as particle labels and
for a quantum group appearing beside them. Contrast: the $q$ there is fitted against baryon
masses, which this repo's anti-fit rule forbids, and it is not the braiding parameter.

### 2. Chester, Arsiwalla, Kauffman, *Preons, braid topology, and representations of fundamental particles* (2025)

arXiv:2501.03260v1 [physics.gen-ph], 3 Jan 2025. No journal reference printed. Key
`chester-arsiwalla-kauffman-2025`.

**Summary.** Maps helon states onto the weight lattice of $SU(3)_c \times U(1)_{\mathrm{em}}$, shows
Lambek's 4-vector (rishon) model is recovered from helon diagrams, introduces a 5-vector
representation from the $D_2 \oplus A_2 \oplus A_1$ weight lattice, defines braid analogues of C,
P and T, and reports that among the 16 two-crossing three-strand diagrams only the helon braids are
CPT invariant. Chirality is read through $B_3 \to PSL(2,\mathbb{Z}) \subset PSL(2,\mathbb{C})$.
The authors state that the helon model captures only the unbroken $SU(3)_c \times U(1)_{\mathrm{em}}$
sector and lacks a projector for the left-handed weak interaction. Their Table 2 gives, for
example, $e_L \mapsto \sigma_1^{-1}\sigma_2 T^{-1}_{123}$.

**Colour.** Twist data on the $A_2$ weight lattice. For composites they introduce
*colour-matched braid multiplication*: colour is not fixed to a strand position; it is assigned to
the first factor and then **follows each strand through the permutation**, so whole strands keep
one colour. Without that rule three red quarks look colourless.

**q.** None. Classical $B_3$; no Hecke algebra, no Jones polynomial, no Markov trace (the three
hits for "q-deformed" / "quantum group" in the text are bibliography entries).

**Relation: precedent and sharp contrast.** It is the most recent survey of how braid models get
$SU(3)_c$. Its colour-matched multiplication is exactly the "colour moves with the strand" move.
On branch `claude/qcd-heat-kernel-beta0-sign-2026-11-22` (PR #9059, unmerged), probe
`computations/probes/qcd_colour_action/` found that, in the searched class where colour acts
strand-wise and commutes with the crossing, a Hecke braiding that carries colour with the strand
satisfies the braid relation only at $p^2 = 1$, $q^2 = 1$ (lex Gröbner basis
$\{(p^2-1)^2, (q^2-1)^2\}$). So their rule is consistent with that result precisely because they
work at the classical point. That is a statement about an unmerged probe inside a named class; it
is **not** written into the content block.

### 3. Gresnigt, *Braids, normed division algebras, and Standard Model symmetries* (2018)

arXiv:1803.02202v2 [physics.gen-ph], 16 Mar 2018. Page 1: "Prepared for submission to JHEP"; no
journal reference printed, none added. Key `gresnigt2018`.

**Summary.** Each normed division algebra represents a circular braid group; for $\mathbb{C}$ and
$\mathbb{H}$ these are $B_2$ and $B_3^c$. Helon framed braids can be rewritten as pure braid words
in $B_3^c$ with trivial twisting, and these coincide with the basis states of the minimal left ideals
of $\mathbb{C}\otimes\mathbb{O} \cong C\ell(6)$, which (following Furey) carry one generation under
unbroken $SU(3)_c \times U(1)_{\mathrm{em}}$. The neutrino idempotent corresponds to the trivial
braid, a stated tension with the helon model.

**Colour.** Inherited from the octonion ideals; braids are identified with their basis states.

**q.** None in the braiding (the braided ribbon networks it mentions are $q$-deformed spin networks,
but no $q$ enters the constructions here).

**Relation: precedent, and the route not taken.** It shows that colour in braid-preon models comes
from outside the braid group.

### 4. Balagović, Kolb, *Universal K-matrix for quantum symmetric pairs* (2015)

arXiv:1507.06276v2 [math.QA], 29 Jan 2016. No journal reference printed. Key
`balagovic-kolb-2015`.

**Summary (abstract and §1.1).** For $\mathfrak{g}$ of finite type, the quantum symmetric pair
coideal subalgebras $B_{c,s} \subset U_q(\mathfrak{g})$ have a universal K-matrix: an element of a
completion of $U_q(\mathfrak{g})$ commuting with $B_{c,s}$ and solving the reflection equation in
every integrable category-$\mathcal{O}$ module. This realises tom Dieck and Häring-Oldenburg's
programme of ribbons in a cylinder (type-B braids). Generic $q$.

**Relation: route not taken (yet).** Not particle prior art. It is the braid-side half of the one
literature route past the $q^2 = 1$ obstruction above: a coideal subalgebra is not a Hopf
subalgebra, so it need not act strand-wise, and its braid partner is the cylinder (type-B) braid
group with a K-matrix, not type-A $H_n(q)$. PR #9059's `qcd_coideal_colour/` has a
pre-registration only; no result.

### 5. Letzter, *Coideal subalgebras and quantum symmetric pairs* (2001)

arXiv:math/0103228v2 [math.QA], 9 Apr 2002. No journal reference printed. Key `letzter2001`.

**Summary.** Survey with selected proofs: coideal subalgebras of $U_q(\mathfrak{g})$, generators,
Harish-Chandra modules, quantum homogeneous spaces, the locally finite part, and the coideals that
are quantum analogues of $U(\mathfrak{g}^\theta)$ for a symmetric pair. Generic $q$.

**Relation: route not taken (yet).** The algebra-side half of the same route. Caution from the
probe notes: the fixed-point subalgebras of $\mathfrak{gl}_3$ symmetric pairs are
$\mathfrak{so}_3$ or $\mathfrak{gl}_2 \oplus \mathfrak{gl}_1$, smaller than $\mathfrak{gl}_3$, so
a coideal colour would itself be a broken colour.

## Verdicts

| paper | add to intro? | why |
|---|---|---|
| Gresnigt 2017 | **yes** | braid groups from $\mathbb{C},\mathbb{H}$; and the fitted root-of-unity $SU_q(3)$ is the clearest contrast with generic $q$ |
| Chester–Arsiwalla–Kauffman 2025 | **yes** | current state of braid preons; states the $SU(3)_c\times U(1)_{\mathrm{em}}$ limit |
| Gresnigt 2018 | **yes** | braid states = octonionic ideal states; colour imported from a division algebra |
| Balagović–Kolb 2015 | **not now** (registered, not cited) | mathematics for a colour route the chapter does not take; cite it where a coideal construction lands, if it does |
| Letzter 2001 | **not now** (registered, not cited) | same |

Also added to the prose, from papers already held: `bilson-thompson2005`, `bilsonthompson2007`,
`kauffman-lomonaco-2007` and `finkelstein2008` (the one braid/knot-preon model with a quantum
group in the knot sector). `gresnigt2019`, `gresnigt2023` and `furey2018` were left out of the
prose: their content was not re-read here, and the Furey result Gresnigt relies on is an earlier
paper than `furey2018`.

## Recommendation (judgement)

Add two paragraphs to `prose:knotted-particles-history`, after the Avrin sentence and before the
closing paragraph: one on the braid-preon lineage, one on the contrast (group vs Hecke algebra,
where $q$ sits, where colour comes from), ending on the photon as a linear combination. Keep
quantum symmetric pairs out of the intro until a construction uses them. Do not mention the
$q^2 = 1$ probe or the convention-D radical in the content: PR #9059 is unmerged and those are
class-limited probe results.

## Proposed prose (as committed)

> A second lineage replaces knots by braids. Bilson-Thompson represented the first-generation
> fermions and the electroweak bosons by braids of three ribbons with two crossings, reading
> electric charge off the twists of the ribbons and colour off the permutations of those twists
> among the ribbons \cite{bilson-thompson2005}. Bilson-Thompson, Markopoulou and Smolin then
> embedded these braids in the braided ribbon networks of quantum gravity
> \cite{bilsonthompson2007}. Gresnigt used the Clifford braiding theorem of Kauffman and Lomonaco
> \cite{kauffman-lomonaco-2007} to show that the complex numbers and the quaternions carry
> representations of exactly the two braid groups of that model, the braid group $B_2$ of the
> twists and the circular braid group $B_3^c$ of the ribbons \cite{gresnigt2017}. He then
> identified the framed braids with the basis states of the minimal left ideals of the complex
> octonions, which, following Furey, carry one generation of leptons and quarks under the unbroken
> symmetry $SU(3)_c \times U(1)_{\mathrm{em}}$ \cite{gresnigt2018}. Chester, Arsiwalla and Kauffman
> mapped the twists of the same states onto the weight lattice of
> $SU(3)_c \times U(1)_{\mathrm{em}}$ and the crossings onto chirality through the homomorphism
> $B_3 \to PSL(2,\mathbb{Z})$, and observed that the model captures only that unbroken sector
> \cite{chester-arsiwalla-kauffman-2025}. Finkelstein kept a deformation parameter: he matched the
> four classes of first-generation fermions with the four trefoils, read as irreducible
> representations of the quantum group $SL_q(2)$ \cite{finkelstein2008}.
>
> In these programmes the braid acts through a group, the classical braid group $B_3$ or its
> circular version with the framing carried by $B_2$, and a deformation parameter, where one
> appears, sits beside the braiding rather than in it. In Gresnigt's review the quantum group
> $SU_q(3)$ is a flavour symmetry, with $q$ a root of unity chosen to fit the octet and decuplet
> baryon masses \cite{gresnigt2017}; in Finkelstein's model $q$ deforms $SL(2)$, the symmetry of
> the knot. Colour is either a label carried by the strands or an import from a division algebra.
> This chapter reads the braid word in the Iwahori–Hecke algebra $H_n(q)$ with $q$ a formal
> parameter, where every generator satisfies $\sigma_i - \sigma_i^{-1} = (q - q^{-1})\mathbf{1}$,
> and evaluates closures with a Markov trace. A particle can then be a linear combination of braid
> words rather than a single braid, as the four-term [photon](#def:photon) is.

## Ingest

The five PDFs were ingested with `cat-harness-tools/scripts/pdf-structure.py` (pypdf backend; the
`bun run cat ingest` entry point does not load on the light platform: missing `liquidjs`) and
`extract-candidates.py`, then `scripts/summarize-library.py --apply`. Only the five new directories
and `library/INDEX.md` are committed; the regenerator also rewrote ~760 unrelated `summary.json` and
section files, which were reverted as out of scope.

| doc-id | pages | section files | body bytes | pypdf text bytes | candidates |
|---|---|---|---|---|---|
| `arxiv-1711.09011v1` | 10 | 12 | 25,445 | 25,389 | 0 |
| `arxiv-2501.03260v1` | 32 | 14 | 82,781 | 81,392 | 1 |
| `arxiv-1803.02202v2` | 21 | 18 | 48,228 | 46,497 | 0 |
| `arxiv-1507.06276v2` | 52 | 42 | 133,962 | 126,780 | 59 |
| `arxiv-math-0103228v2` | 62 | 8 | 129,058 | 121,953 | 47 |

Known defects, reported rather than patched:

- **Run-in headings lose their first line.** In `arxiv-1507.06276v2` (amsart style), 21 of 42
  section files start mid-sentence: the line carrying a run-in heading such as
  "1.1. Background. Let g be … and θ : g → g an" is consumed as the heading. One line per section
  is lost. One file each in `2501.03260v1` and `1803.02202v2` shows the same sign.
- **Three section files are empty by structure**: parent headings ("1 Introduction",
  "4 Normed division algebra representations…", "5 Helon braids…") whose text is in the next
  subsection. Not stubs.
- **Inferred TOCs merge sections.** `1711.09011v1` §2 ($SU_q(3)$ flavour) is inside the
  "1 Introduction" file; Letzter's introduction is inside `sec-front-matter.md`. The text is present.
- No scanned pages; the OCR-skip bug (cat-harness-tools PR 2498) does not apply.

INDEX invariant after the ingest: 803 directories − 778 rows = 25 = 23 duplicates + 1 container
(`ant-v14-n7-s`) + `codata-2022`, which has no `structure.json` and predates this change.
