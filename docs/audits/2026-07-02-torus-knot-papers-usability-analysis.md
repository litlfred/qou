# Torus-knot reference papers — usability analysis (2026-07-02)

Two papers were uploaded to `uploads/` (commits `9e2c2d2a`, `1088902c`):

1. **Murakami, H.** *Asymptotic behaviors of the colored Jones polynomials of a
   torus knot* (arXiv:math/0405126; Internat. J. Math. 15 (2004) 547–555) —
   [uploads/0405126v1.pdf](../../uploads/0405126v1.pdf). Bib key
   `murakami-torus-2004` (added by this audit).
2. **Avrin, J. S.** *Knots on a Torus: A Model of the Elementary Particles*
   (Symmetry 2012, 4(1), 39–115, doi:10.3390/sym4010039) —
   [uploads/symmetry-04-00039-v3.pdf](../../uploads/symmetry-04-00039-v3.pdf).
   Bib key `avrin-2012` (already present in `content/schema/references.ts`;
   the upload supplies the in-repo source for the bib-human-review ladder).

This audit maps both papers against the corpus's torus-knot / Vol=0 sites and
open derivation gaps, and records gap-by-gap verdicts. Negative verdicts are
scope-classified per the AGENTS.md refuted-discipline: **(a)** =
construction-limited, **(b)** = structural exclusion with a cited invariant.

## 1. What Murakami math/0405126 proves (precise statements)

Let $J_N(K;t)$ be the colored Jones polynomial normalized to
$J_N(\text{unknot};t)=1$, and $T(a,b)$ the $(a,b)$-torus knot, $a,b>1$
coprime. Murakami's Theorem 1.1: there is a neighborhood $U$ of $1\in\mathbb{C}$
such that for $r \in U$, $r \notin \mathbb{R}$,

$$
\lim_{N\to\infty} J_N\bigl(T(a,b);\,e^{2\pi i r/N}\bigr)
= \frac{1}{\Delta\bigl(T(a,b);\,e^{2\pi i r}\bigr)}
\qquad \text{if } \operatorname{Im} r < 0,
$$

where $\Delta$ is the Alexander polynomial, and

$$
\lim_{N\to\infty} \frac{\log J_N\bigl(T(a,b);\,e^{2\pi i r/N}\bigr)}{N}
= \Bigl(1 - \frac{1}{2\,a\,b\,r} - \frac{a\,b\,r}{2}\Bigr)\pi i
\qquad \text{if } \operatorname{Im} r > 0
$$

(exponential growth, since the real part of the right side is positive).
The limit is **discontinuous across real $r$** — it "cannot be extended to a
continuous function of $r$" — so the Neumann–Zagier-potential extraction of
volume + Chern–Simons that works for the figure-eight knot (Murakami–Yokota)
**fails structurally for every torus knot**. Supporting facts collected in the
paper:

- **Kashaev–Tirkkonen** [`kashaev-tirkkonen2000`]: at $r=1$ (the Kashaev
  point) $\bigl|J_N(T(a,b);e^{2\pi i/N})\bigr| \sim C\,N^{3/2}$ — polynomial,
  not exponential, growth; $\lim \log|J_N|/N = 0$, matching Gromov norm $0$
  of the Seifert-fibered complement. This **proves the volume conjecture for
  torus knots** (trivially: both sides are $0$).
- **Hikami–Kirillov** [`hikami-kirillov2003`]: the *phase* of the $r=1$
  asymptotics relates to the $SU(2)$ Chern–Simons invariant of the Seifert
  space (minimal-model CFT data). The residue expansion (Murakami eq. (2.2))
  produces the family of rational phases $k\pi i\bigl(1-\tfrac{k}{2abr}\bigr)$,
  $0<k<ab|r|h(\theta)$, $a\nmid k$, $b\nmid k$ — the classical CS values
  $-k^2/(4ab)$ of flat connections on torus-knot surgeries.
- **Melvin–Morton–Rozansky** (proved by Bar-Natan–Garoufalidis
  [`bar-natan-garoufalidis1996`]): the diagonal $h$-expansion coefficients of
  $J_N(K;e^h)$ give $1/\Delta(K;e^{hN})$ for **every** knot. Murakami's
  Theorem 1.1 (Im $r<0$ branch) says that for torus knots the full limit
  *equals* the MMR diagonal — nothing beyond the Alexander polynomial
  survives — whereas for the figure-eight it does not (the volume term
  dominates).
- **Hikami's recursion** (Comment 3.2): $J_N(T(a,b);t)$ satisfies an explicit
  two-term $q$-holonomic recursion — closed-form AJ-style machinery exists
  for the whole $T(2,2k+1)$ tower.

## 2. Corpus state being audited (summary of the survey)

The corpus assigns torus knots three inconsistent mass treatments:

| Site | Treatment | Status |
|---|---|---|
| `content/quantum-observable-universe/mass-theory/topological-mass-trefoil.md` | trefoil-electron mass via $\mathrm{Li}_2(q^{-2})/\hbar_q^2$, claiming the quantum dilog "interpolates between the classical volume … and the Chern–Simons invariant" | **contradicts** the §7b / hyperbolic-hurdle audits (see V1) |
| `computations/meson_vol_density.py`, `mass-theory/gen3-meson-phi-hecke-seifert.md` | mesons bypass Vol: $H_3$ Frobenius pairing + Seifert surrogate $V_S(T(2,n)) = \pi(n-2)/n$ | ad-hoc but numerically anchored (φ(1020) at 2167 ppm via $V_S$ ratio $15/7$) |
| `lean/QOU/BraidKnot/TorusKnotMass.lean` | scaffold class, `sorry` instance: "the torus-knot mass derivation requires a DIFFERENT chain" | open by design |

Plus one active probe (`computations/delta_lambda_alexander_phase4.py`)
substituting $V(K) = |\Delta_K(t)|$ for Seifert pieces, and the resolved-but-
underived muon identification (`docs/audits/2026-06-30-muon-knot-id-phi-q-evidence.md`:
$\mu = T(2,5)$, $4_1$ = Higgs, coupling scale $\mathrm{Vol}(4_1)/\hbar_q^2$).

## 3. Gap-by-gap verdicts

### V1 — Trefoil dilog "interpolation" claim: now refutable by citation (upgrade to (b))

`topological-mass-trefoil.md` asserts the quantum dilogarithm "interpolates
between the classical volume (for hyperbolic knots) and the Chern–Simons
invariant (for non-hyperbolic knots such as torus knots)" and assigns
$\mathfrak{m}(\tau(2,3)) = \mathrm{Li}_2(q^{-2})/\hbar_q^2$. The corpus already
brands trefoil-dilog arguments a recurrent failure mode
(AGENTS.md §7b; `docs/audits/2026-06-16-hyperbolic-hurdle-dialog-assessment.md`),
but only as repo-internal lore (Seifert-fibered ⇒ $D(z)=0$).

**Murakami Theorem 1.1 supplies the published invariant that upgrades this to
a proper (b)-scope structural exclusion**: the colored-Jones asymptotics of a
torus knot contain *no volume-like continuous limit in any deformation
neighborhood of the Kashaev point* — the limit function is discontinuous in
$r$, polynomially bounded at $r=1$, and equal to $1/\Delta$ on the
$\operatorname{Im} r<0$ side. There is no interpolating dilog object for the
trefoil to evaluate; whatever $\mathrm{Li}_2(q^{-2})/\hbar_q^2$ is, it is not
the torus-knot limit of the Kashaev/archimedean-realization chain that
justifies $\mathrm{Vol}$ for hyperbolic knots
(`rem:kashaev-as-archimedean-realization`).

- **Scope note (what is NOT excluded):** the numerical *value* the block wants
  for the electron is not refuted — only the *derivation route* "torus-knot
  colored-Jones asymptotics → volume-like mass" is excluded. A different chain
  (per `TorusKnotMass.lean`'s honest framing, or the Alexander route of V2)
  remains open. This is exactly the (a)-vs-(b) split: route (b)-excluded,
  target (a)-open.
- **Action:** follow-up bean filed to re-scope the block's prose (cite
  `murakami-torus-2004`; keep the $4_1$/Higgs half, which is consistent with
  the 2026-06-30 muon-ID audit). Content-block edit deferred to a follow-up
  since it touches a mass-theory claim the owner should sign off on.

### V2 — Alexander Phase-4 substitution: upgraded from ansatz to theorem-backed

`delta_lambda_alexander_phase4.py` replaces the degenerate hyperbolic volume
of Seifert-fibered pieces by $V(K) = |\mathrm{Alex}_K(t)|$ (Burau-computed),
evaluated at $t \in \{-1,\ q_0,\ q_0^2\}$. Before this upload the substitution
was a plausible ansatz. **Murakami Theorem 1.1 makes it canonical in shape**:
the *actual* limit of the same colored-Jones object that produces
$\mathrm{Vol}$ on the hyperbolic stratum is $1/\Delta(T(a,b);e^{2\pi i r})$ on
the torus stratum. I.e. the archimedean-realization functor, restricted to
Seifert-fibered closures, *is* (inverse-)Alexander evaluation — the
substitution is the same $\tau_{\mathrm{arch}}$ limit read on the other
stratum, not a new mechanism.

Two corrections the theorem forces on the probe design:

1. **Orientation:** the limit is $1/\Delta$, not $\Delta$. A per-knot factor
   built from $|\Delta_K|$ should be tested in both orientations, with the
   inverse as the theorem-preferred default.
2. **Evaluation point:** the limit object is $\Delta$ evaluated on the unit
   circle $e^{2\pi i r}$ ($r$ near 1), not at real $q_0$. A real-$q_0$
   evaluation is a further analytic continuation that the theorem does not
   cover — fine as exploration, but the circle evaluation is the derived one.

### V3 — Two-branch discontinuity ↔ the corpus's bar-involution wall (structural corroboration)

The two half-planes $\operatorname{Im} r \gtrless 0$ exchange under
$r \mapsto \bar r$, i.e. under the bar involution $q \mapsto q^{-1}$, and the
two limits differ **discontinuously** (inverse-Alexander vs exponential
CS-phase growth). This is a rigorous, published instance of the corpus's
"Im(q) at fibre vs observable level" two-level framing (AGENTS.md banner) and
of the bar-even/bar-odd split driving `conj:binding-qbeta-complex-volume`
(binding = bar-even / $Q_\beta$ = bar-odd branches of one complex volume; cf.
PR #3204's $q_0$ vs $q_0^{-1}$ ladder probe). For torus knots the two branches
are *maximally* split: one is rational (Alexander), the other is a pure CS
phase. Usable as a literature anchor when writing up the two-branch structure;
it does not by itself prove anything about the nuclear ladders.

### V4 — Muon knot-ID and generation modulation (supports; opens one narrow probe)

The 2026-06-30 resolution ($\mu = T(2,5)$, $4_1$ = Higgs) is *strengthened*:
by Theorem 1.1, $T(2,5)$ has no volume asymptotics at any nearby $r$, so the
muon mass **cannot** be its own knot's volume — the Higgs-coupling framing
(mass scale $\mathrm{Vol}(4_1)/\hbar_q^2$ common to all generations) is the
only Vol-consistent reading. The open question there ("how does the generation
index $T(2,3)/T(2,5)/T(2,7)$ modulate the common coupling?") now has a
theorem-supplied candidate object: the generation-dependent invariant that
survives the torus-stratum limit is $1/\Delta(T(2,n);e^{2\pi i r})$, whose
zeros sit at primitive $2n$-th roots of unity — a cyclotomic structure indexed
by the generation. **Formalize-first caveat:** testing "lepton ratios ∝
inverse-Alexander data" over evaluation points would be a wide scan; per
`compute-author §3.3` the class must first be narrowed by a structural
constraint (e.g. bar-symmetry + the three-calibration discipline forbid new
anchors; only parameter-free evaluations at already-canonical points
$e^{2\pi i r}$, $r \to 1$, are admissible). Filed as a bean with that
constraint stated; **no scan run in this session.**

### V5 — Meson Seifert surrogate $V_S = \pi(n-2)/n$: no immediate upgrade (two quick negatives, scope (a))

The gen-3 meson block matches φ(1020) via
$V_S(T(2,7))/V_S(T(2,3)) = (5/7)/(1/3) = 15/7$. Murakami's asymptotics offer
two obvious parameter-free phase families that might have *derived* $V_S$;
both fail numerically (checked by hand, exact rationals):

- saddle-exponent coefficient $1 - \tfrac{1}{2ab} - \tfrac{ab}{2}$ at $r=1$:
  ratio $T(2,7)/T(2,3) = \tfrac{169/28}{25/12} = \tfrac{507}{175} \approx 2.897 \neq 15/7 \approx 2.143$;
- leading residue phase $1 - \tfrac{1}{2ab}$ (k=1):
  ratio $= \tfrac{27/28}{11/12} = \tfrac{81}{77} \approx 1.052 \neq 15/7$.

**Scope (a):** these two specific phase candidates, alone, do not reproduce the
$V_S$ ratio. The full residue family $k^2/(4ab)$ (all admissible $k$) and the
Hikami–Kirillov minimal-model weights remain unexplored as a derivation of
$V_S$; that is the right-sized follow-up probe (small, finite, decisive per
knot pair) and is beaned.

### V6 — $c_k$ ladder (G5): not reopened

The torus-knot hypothesis class for the $Q_\beta$ $c_k$ coefficients was
already eliminated
(`docs/audits/2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md`), and
nothing in Murakami's theorem reopens it: the theorem produces per-knot
constants at fixed $r$, not a scaling map in $u = b\hbar_q^2$. The open axis
there (Habiro element / Ohtsuki expansion) is *adjacent* — Murakami's
$\operatorname{Im} r>0$ exponent is the type of object that lives in the
Habiro-ring story — but the paper contains no $c_k$-shaped result. No action.

### V7 — s5-so3 keystone (G2): technique-level relevance + source note for sibling s013

The keystone's open object is the colored $\Sigma(2,3,5)$ WRT / Lawrence–
Rozansky amplitude (Seifert-fibered CS localization). Murakami's proof
technique — integral form, residue family = flat-connection CS values, saddle
= trivial-connection contribution — is exactly the Seifert-asymptotics toolkit
(Lawrence–Zagier, Hikami) that sibling PR #3208 (bean `s013`) reported as
**literature-gated** ("primary sources firewalled … no copies in uploads/").
The uploaded Murakami paper is not the missing Hikami/Andersen–Mistegård
sources, but it is an in-repo worked example of the residue-vs-saddle split
for Seifert asymptotics, with the Hikami–Kirillov reference chain. Noted on
the sibling PR.

### V8 — Unassigned generators $T_{2,9}$, $T_{3,5}$: marginal help

Per-generator Alexander data and growth exponents ($ab = 18$, $15$) are now
citable inputs to the Skein-interaction comparison requested in
`predicted-spectra/unmapped-torus-knots.md` §Open problem. No assignment made
here.

## 4. Avrin (Symmetry 2012) — usability

Already in the bibliography (`avrin-2012`) with an accurate prior-art note
(torus-knot generational skeleton has precedent; QOU's Hecke/Markov-trace +
complex-volume + Askey formalization is the novel content). What the upload
adds / enables:

1. **Source-in-repo** for the bib-human-review ladder — the PDF is now the
   in-repo source backing the `avrin-2012` entry.
2. **Prior-art differentiation table** (for the related-work prose, when
   written): Avrin's model is *qualitative* — unknot + trefoil as flattened
   Möbius strips, fusion algebra (§3–5), boson matrix (§7.4), three
   generations via twist scaffolds (§8) — with **no quantitative mass
   derivation, no Hecke algebra, no Markov trace, no calibration discipline**.
   Charge arises as thirds from crossing counts; QOU derives observables to
   ppb-scale from three calibrations. The overlap is the $T(2,2k+1)$
   generation skeleton (Avrin's fermion tower ↔ QOU's
   `lepton-meson-torus-knot-dictionary.lean` $e = T(2,3)$, $\mu = T(2,5)$,
   $\tau = T(2,7)$), which is *independent motivation* for the dictionary, and
   useful to cite adversarially (preempts "this was done before" — it was, at
   the qualitative level, and the paper says so).
3. **Boson-matrix cross-check** (speculative, unbeaned): Avrin §7.4's fusion
   boson matrix could be compared against the Skein interaction terms once the
   $T_{2,9}/T_{3,5}$ gauge-boson computation (V8) is attempted; recorded here
   only as a pointer.

Avrin closes no derivation gap (it contains no derivations of QOU type).

## 5. Bottom line

- **No open derivation gap is closed outright by these papers.** (Expected: a
  citation cannot discharge a `sorry`.)
- **One justification gap closes:** the "no volume-route mass for torus knots"
  guardrail is upgraded from repo-lore to a citable published theorem
  (`murakami-torus-2004` + `kashaev-tirkkonen2000`), giving the §7b failure
  mode a proper (b)-scope invariant.
- **One live inconsistency exposed:** `topological-mass-trefoil.md`'s
  $\mathrm{Li}_2$ interpolation sentence is now refutable by citation (V1);
  re-scope beaned for owner sign-off.
- **One active probe upgraded:** the Alexander Phase-4 substitution is the
  theorem-preferred realization of $\tau_{\mathrm{arch}}$ on the Seifert
  stratum, with two design corrections (inverse orientation; unit-circle
  evaluation) (V2).
- **Two quick negatives recorded** at scope (a) (V5) and two narrow,
  formalize-first-gated probe beans filed (V4, V5).
- **Citation upgrades:** `kashaev-volume-conjecture.md` ("proved only for …
  certain torus … knots") can now cite `kashaev-tirkkonen2000` precisely; the
  torus-knot h-expansion audit's "MMR-like" reasoning gets its missing key
  `bar-natan-garoufalidis1996`.

## 6. Actions taken in this PR

- This audit doc.
- `content/schema/references.ts`: added `murakami-torus-2004`,
  `kashaev-tirkkonen2000`, `bar-natan-garoufalidis1996`,
  `hikami-kirillov2003` (bibliographic data cross-checked against the
  uploaded PDF's reference list; doi.org is firewalled in this sandbox, so
  DOIs are included only where high-confidence and are flagged as not
  machine-verified in the entry notes).
- Follow-up beans: V1 re-scope (owner-gated), V4 generation-modulation
  formalize-first probe, V5 residue-family $V_S$ derivation probe.
- `uploads/intake.json` registration **skipped**: the file is a single-document
  legacy record (UGB paper), not a registry; the flat-PDF uploads in
  `uploads/` follow no intake convention to extend. Flagged here instead.
