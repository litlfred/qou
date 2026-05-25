This audit catalogues every place in the mass, beta-decay, and
binding-energy computations of the Quantum Observable Universe framework
where the derivation relies on empirical data, fitting, numerology, or
an unproven assumption rather than on a completed categorical derivation.

**Pre-approved calibration inputs** (NOT flagged):

See [Table 1](#tbl:derivation-audit-report-table1-data).

**Gap categories:**
- **GAP-A** Missing categorical derivation (formula used without proof from categorical axioms)
- **GAP-B** Empirical fitting (parameter fitted to data rather than derived)
- **GAP-C** Numerology/pattern match ($q$-integer product matches experimental value but derivation not shown)
- **GAP-D** Open conjecture backing (computation rests on an unproved assumption)

---

## GAP-A-1 — Canonical knot identification for $^2$H, $^3$H, $^3$He

**Source:** `atom-knot-mass-derivation.md`, pipeline step "Confinement SDP".

**Description.**  The canonical Hecke elements $T_w$ for the light
nuclei deuterium ($^2$H = $6_2$), tritium ($^3$H = $8_{11}$), and
helium-3 ($^3$He = $L_{6a4}$) were identified historically by matching
hyperbolic volumes to AME binding energies, not by executing the
categorical confinement SDP from first principles.  The SDP pipeline
([prop:confinement-sdp](#prop:confinement-sdp)) is defined, but the
proof that it *selects* these specific knots as its unique minimizers
(at $\rho = 1$ for $^2$H and $\rho = 2$ for $^3$H/$^3$He) has not been
completed.

**Resolution path.**  A conjecture stating the SDP uniqueness result
has been created:
[conj:canonical-knot-id-sdp](#conj:canonical-knot-id-sdp).

---

## GAP-A-2 — Chirality formula $a_K = 1 + w \cdot h$ (chiral case) *(refined 2026-05-09)*

**Source:** [`chirality-writhe-ribbon-derivation.md`](chirality-writhe-ribbon-derivation.md) §Caveat and §Numerical test at $H_6(R, q)$ (satellite $D$).

**Status:** **Refined.** The structural form
$a_K = 1 + w(\beta) \cdot X \cdot h + O(h^2)$ is retained (linear
in $h$ and writhe), but the specific coefficient
$X = \langle c \rangle_\beta$ (Wedderburn-averaged content) is now
**numerically falsified** on the deuteron. The script
[`folio-assistant/computations/_deprecated/ribbon_content_average.py`](../../../folio-assistant/computations/_deprecated/ribbon_content_average.py)
computes $\langle c \rangle_\beta$ and the predicted $a_D$, giving
values that vary from $-2.16$ to $+3.10$ depending on whether
inter-nucleon crossings are included, against paper's assignment
$a_D = 1 + h \approx 1.21$. (Witness:
[`_deprecated/ribbon-content-average.witness.json`](../../../folio-assistant/computations/_deprecated/ribbon-content-average.witness.json).)
The single-nucleon neutron case happens to land within $2.5\%$
"coincidentally close but without deeper structural justification at
$A = 1$" (quoting [`chirality-writhe-ribbon-derivation.md`](chirality-writhe-ribbon-derivation.md)).
The Wedderburn-averaged coefficient is therefore **not** the
correct $X$; possible refinements (weighting by $\dim_q(\lambda)$
instead of $\dim_q(\lambda)^2$, topological vs. algebraic writhe,
true Hecke ribbon element) are listed in the source block.

The structural form (linear-in-$h$, conditional on chirality of
the underlying braid) has been **reduced** to a finite crystal-graph
computation via Type-B folding (Brundan-Kleshchev cyclotomic KLR +
Lecouvey GS / crystal-highest-weight bijection); see
[`../archimedean-universe/crystal-basis-resolves-mass-tower-open-problems.md`](../archimedean-universe/crystal-basis-resolves-mass-tower-open-problems.md)
§"Reduction 1: chirality $\langle c \rangle_\beta$ via Type-B folding".
The reduction is *sorry-free conditional* on
[`brundankleshchev2009`] + [`lecouvey2007`]; the residual open
content is the explicit crystal-graph computation.

**Resolution path.**  [conj:chirality-ribbon-frobenius](#conj:chirality-ribbon-frobenius)
states the complete form and flags the proof obligations.

---

## GAP-A-3 — Brane-tower level-selection rule $n_\star(\mathfrak{H})$

**Source:** `brane-tower-z-habiro.md` §Statement.

**Description.**  The brane-tower regularization requires a canonical
level-selection rule $n_\star : \{\text{confined particles}\} \to \mathbb{N}$
that is derivable from QOU substrate data alone.  The conjecture
([conj:brane-tower-z-habiro](#conj:brane-tower-z-habiro)) states its
existence, but no formula for $n_\star$ has been derived.  For low
isotopes the truncation depth was chosen by matching empirical binding
energies (GAP-B overlap); for heavier nuclei no rule is specified.

**Resolution path.**  [conj:brane-level-selection](#conj:brane-level-selection)
isolates the level-selection sub-problem from the broader Habiro
convergence conjecture.

---

## GAP-A-4 — Structural prefactor $\rho(Z, N)$ general rule

**Source:** `atom-knot-mass-derivation.md` §Architecture, note on SDP multiplicity.

**Description.**  The SDP multiplicity $\rho \in \mathbb{Z}_{>0}$ for
a nucleus $(Z, N)$ is found as a by-product of the Wedderburn SDP
witness (e.g. $\rho = 1$ for $D$, $\rho = 2$ for $T$ and $^3$He).
No general derivation of $\rho(Z, N)$ from the categorical data alone
(confinement level $\ell$, strand count $n_0$, quark flavors) has been
given.  Individual values are discovered by running the SDP numerically,
which is an empirical search, not a derivation.

**Resolution path.**  [conj:rho-prefactor-structural](#conj:rho-prefactor-structural)
frames the conjecture.

---

## GAP-A-5 — Binding gap for light isotopes $A \geq 5$

**Source:** `derived-mass-formula-light-isotopes.md` §Note on $^6$Li, $^7$Li.

**Description.**  The derived mass formula for light isotopes
([prop:derived-mass-formula-light-isotopes](#prop:derived-mass-formula-light-isotopes))
is validated for $A \leq 4$ (no fitting, zero free parameters).  The
extension to $^6$Li and $^7$Li is described as a "predictive" extension,
but the knot-atlas entries for $A = 5, 6, 7$ isotopes are not yet
produced by the categorical SDP; they rely on the recursive atom-knot atlas,
which itself is only proved to be complete for $A \leq 60$ under
Plancherel-bound certificates — not from a first-principles completeness
theorem.

**Resolution path.**  The recursive-atlas completeness proof is needed;
this is flagged as an open sub-problem (see `recursive-atom-knot-atlas` block).

---

## GAP-B-1 — Per-nucleon scaling between $A = 2$ and $A = 3$ *(closed 2026-05-09)*

**Source:** `commutative-crossing-energy.md` §Caveat.

**Status:** **Closed** by the Path A pipeline (commits `f9f25b5f`,
`23e447dc`, `per_irrep_pole_atom.py`).  The structural form of the
per-nucleon scaling between $A = 2$ and $A = 3$ is now categorically
derived: symbolic Hoefsmit pole-order analysis verifies
$\mathrm{ord}_{u=0}(\mathrm{tr}_M(\beta)) = 18Z + 21N + 1$ for proton
($Z=1, N=0$) and deuteron ($Z=N=1$); predictions then agree with
experimental atomic masses to $\leq 0.30\%$ across $Z = 1\ldots 20$
via the single-generator $\rho_K$ formula (witness:
`rho-k-pair-gen-v2-wedderburn.witness.json`).  See the explicit
"Caveat (updated 2026-05-09)" paragraph in
`commutative-crossing-energy.md`.

**Description (historical).**  The proposition originally derived the
binding scale from Hecke-algebra structure but explicitly noted: "the
per-nucleon scaling between $A = 2$ and $A = 3$ remains underived."
The numerical coefficient relating deuterium binding to tritium/helium-3
binding was an empirical fit at that stage.

---

## GAP-B-2 — Fitted $\beta_3$ in atomic braid mass *(closed)*

**Source:** `content/quantum-observable-universe/particle-interactions/atomic-braid-mass.md`
§Definition (block moved from `braids-and-knots/`).

**Status:** **Closed.**  The coefficient is now derived in closed form
as $\beta_3 = (q - q^{-1})^2 \approx 0.0437$ at the substrate value
(see
[`particle-interactions/atomic-braid-mass.md`](../particle-interactions/atomic-braid-mass.md)
around line 184).  On the Lean side this is the
`WedderburnMassFormula.β₃ := HA^2` field
([`particle-interactions/atomic-braid-mass.lean`](../particle-interactions/atomic-braid-mass.lean)
around line 77).  The current numerical value
$\approx 0.0437$ differs slightly from the historical fit "$\approx 0.050$"
and is now a derived q-integer-like quantity, not a fit input.

**Description (historical).**  The atomic braid mass formula originally
used an internal parameter $\beta_3 \approx 0.050$ for the
gluon-contribution weight of the third-generator crossing in nucleon
internal structure.  That value was fitted to reproduce proton/neutron
masses rather than derived from the Hecke algebra structure.

---

## GAP-B-3 — Compound $\beta$-decay shell calibration ($y_{\mathrm{target}}$ values) *(closed)*

**Source:** [`compound-beta-shell-calibration.md`](compound-beta-shell-calibration.md).

**Status:** **Closed.** The block is now a proposition
(`prop:compound-beta-shell-calibration`) explicitly stating that
$y_{\mathrm{target}}(A_{\mathrm{magic}})$ is **derivable**, not
independently calibrated, from the cumulative $\beta$-decay chain
reaching the magic anchor. The derivation routes through a chain of
$\beta$-decays along the $\beta$-stability valley, summing $Q_\beta$
values, and yields the magic-shell binding contribution as the
"difference of shell-operator contributions between parent and
daughter, not the shell magnitude itself." Only $E_0 = Q_\beta$
(CAL-3) is consumed as input — no separate $y_{\mathrm{target}}$
calibration. See [`compound-beta-shell-calibration.md`](compound-beta-shell-calibration.md)
§"Compound β-decay principle" for the chain-summing formula.

**Description (historical).**  The compound $\beta$-decay shell
calibration originally used target $y$ values for the Markov-trace
expansion that were calibrated to reproduce a set of measured
$Q$-values, rather than predicted from the categorical derivation
chain. The connection from the abstract $y_\lambda$
([prop:alpha-k-derivation-procedure](#prop:alpha-k-derivation-procedure))
to the shell-model $y_{\mathrm{target}}$ values used in practice
was the open piece; it is now bridged by the chain-summing
derivation described above.

---

## GAP-C-1 — $q$-integer BW coefficients (pattern match)

**Source:** [`../particle-interactions/q-integer-mass-formula.md`](../particle-interactions/q-integer-mass-formula.md) (block moved from `braids-and-knots/`).

**Status:** **Partially derived.** Five standard liquid-drop
coefficients (volume, surface, Coulomb, asymmetry, pairing) and
two extended terms (exchange Coulomb, shell correction) are now
expressed as products of $q$-integers $[n]_q$ evaluated at $q_0$,
times $m_e$, with **0.2–2.1% agreement** to empirical fitted values
(see the per-coefficient table in
[`../particle-interactions/q-integer-mass-formula.md`](../particle-interactions/q-integer-mass-formula.md)).
The block is itself a **Conjecture (BW-emergence)** conditional on
`conj:palindromicity-orbital-type` + `conj:shell-closure-nf-term-count`,
so the closure is *partial-with-conditional-uplift*, not fully derived.

**Description (historical).**  The extended Bethe--Weizsäcker
coefficients are expressed as products of $q$-integers $[n]_q$
evaluated at $q_0$. The proposition notes "derivation of the five
standard terms" from Wedderburn and crossing counts, but the
specific $q$-integer factors (e.g.\ $[7]_q$ from "7 crossings on
generator 0: 3 B$_{3}$ + 1 uu + 2 gluon + 1 ud") rest on counting
arguments whose first-principles derivation within the Hecke
algebra framework lives in the upstream palindromicity and
shell-closure conjectures.  The crossing counts themselves
reproduce known BW values to $< 2\%$ but the categorical-substrate
derivation is conditional on those upstream conjectures.

---

## GAP-D-1 — Energy scale $\mathfrak{E}_0$ predicted vs. calibrated

**Source:** `beta-decay-energy-scale.md`, `negative-debt-confinement.md`.

**Description.**  The leptonic derivation gives
$\mathfrak{E}_0^{(\mathrm{lept})} = m_e/(q_0(q_0-1)) \approx 4.186$ MeV,
while the hadronic calibration gives $\mathfrak{E}_0^{(\mathrm{had})} \approx 4.155$ MeV.
The $0.75\%$ discrepancy is attributed to the brane tower correction,
but the *specific* tower correction that would close this gap has not
been computed.  In the 9-strand ($H_9(q)$) picture the gap should
close, but this is an open direction (noted in `negative-debt-confinement.md`
§Status: the nine-strand direction).

The current hadronic calibration rests on
[conj:brane-tower-z-habiro](#conj:brane-tower-z-habiro) (GAP-D);
once the brane tower is controlled algebraically the $0.75\%$ gap
becomes a computable correction and $Q_\beta$ remains the single
hadronic input for normalization only.

---

## Gap summary table

See [Table 2](#tbl:derivation-audit-report-table2-data).
