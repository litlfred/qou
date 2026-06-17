# Brunnian selection of the confinement operator 𝓑₃ — promote the topological criterion into the program

**Branch:** `claude/borromean-brunnian-selection-2026-06-17`
**Picks up:** #2433 verdict (1), second of its two named non-refuted directions,
after the 2026-06-17 dense-SDP closure
([`2026-06-17-b3-dense-sdp-lever-closed.md`](../audits/2026-06-17-b3-dense-sdp-lever-closed.md))
refuted the *first* (operator-space SDP). Discipline: formalize-first; no fit.

## The problem #2433 left

𝓑₃ must be selected as the 3-quark confinement operator. Two facts now bound the
search:

- **Continuous operator-space selection is refuted** (dense-SDP closure): the SDP
  collapses to "min-eigenvector of cost `T`", and since `NF(𝓑₃)` is **99.8% γ**
  (the max-cost identity channel) every non-fitted `T` selects the *min*-cost
  **mesonic L±** instead. No continuous functional on NF-operator-space reaches
  𝓑₃; only `T = −𝓑₃𝓑₃ᵀ` (a fit) does.
- **The corpus's working selection uses a physical input.** `confinement-
  operator-selection.md` selects 𝓑₃ by `|Δnet|` closest to the target
  `net_proton`, with the Borromean property as an after-the-fact *tiebreak*.
  #2433 flagged the net-target as arguably circular.

## The reframing (this branch's contribution)

The selection **cannot live on NF-operator-space** — there 𝓑₃ is just "mostly
identity", invisible to any extremal functional. It must live on **braid-word /
link space**, where confinement has an input-free meaning:

> **Confinement = no proper subset of the 3 quarks can be isolated = the closure
> is a BRUNNIAN link** (every proper sublink trivially unlinked).

The selection principle is then purely topological + Occam, with **no physical
target and no fitted cost**:

> **Among Brunnian 3-component links, select the crossing-minimal one** — the
> **Borromean rings** = closure of `(σ₁σ₂⁻¹)³`, the unique 6-crossing Brunnian
> link (Rolfsen; the simplest nontrivial Brunnian link).

## What is established (scoping probe, [`b3_brunnian_selection_scope.py`](../../computations/probes/b3_brunnian_selection_scope.py))

The Brunnian signature is verified directly from the braid word (no SnapPy):

| check | result |
|---|---|
| `(σ₁σ₂⁻¹)³` is a **pure** 3-braid (perm = id ⇒ 3 components) | PASS |
| all three pairwise **linking numbers = 0** (Brunnian) | PASS |
| yet every pair still crosses (2 crossings, canceling signs) | PASS |

So "no quark subset isolable" is a **crisp, input-free** constraint: satisfied by
𝓑₃, and **failed by the mesonic L±** channel (a 2-strand pairwise object) that
the operator-space SDP fell into. The Brunnian constraint is exactly the
feasible-set restriction the dense-SDP lacked.

**Spherogram cross-check (stable, kernel-free).** The probe also confirms via
spherogram's exact combinatorial path: the closure of `(σ₁σ₂⁻¹)³` is a 3-component
6-crossing link that **stays at 6 crossings** under Reidemeister `simplify`
(nontrivial), while **every 2-sublink simplifies to 0 crossings** (the unlink) —
a rigorous Brunnian proof, distinguishing the unlink from the Hopf link (which
stays irreducibly at 2) without any float invariant. **The SnapPy numerical
kernel (`.exterior().volume()`, `.identify()`) is deliberately avoided** — a
sibling reported unstable results from it, and it errors `SnapPy doesn't seem to
be available` in this sandbox. Only exact combinatorial invariants are used.

## What remains open (honest)

1. **The candidate is now PROVEN Brunnian + nontrivial at 6 crossings**
   (spherogram, stable path) — but **uniqueness over ALL Brunnian 3-links** (that
   Borromean is *the* crossing-minimal one) is still a literature citation
   (Rolfsen; Brunnian classification), not re-derived. Closing it needs an
   enumeration of Brunnian 3-braids by crossing number confirming uniqueness at 6
   — a finite combinatorial task (braid-word enumeration + the same stable
   simplify-based Brunnian test; **must not** rely on the SnapPy hyperbolic
   kernel, per the instability note above).
2. **Braid-word vs link non-uniqueness.** "Minimal Brunnian 3-link" pins the
   *link* (Borromean) uniquely, but the *braid word* only up to Markov moves;
   `(σ₁σ₂⁻¹)³` is the canonical minimal-length representative. Fine for selecting
   the operator (Markov trace is a conjugacy/Markov invariant), but worth stating.
3. **This does NOT close the binding magnitude.** It resolves the *selection
   principle* (#2433 verdict (1)) — the program should select on link space under
   the Brunnian constraint. The *operator-cumulant scalar extraction* (#2430)
   that would turn 𝓑₃ into a MeV binding remains gated on a non-trace functional;
   the dense-SDP closure did not unlock it and neither does this.

## Skeptical assessment (critical-distance)

- **Genuine improvement:** replaces the circular `net_proton`-target ranking with
  a topological+minimality principle that needs no experimental input. The
  physics map (confinement ⇔ no isolable subset ⇔ Brunnian) is clean and
  motivated, not fitted.
- **But not a magic bullet:** it selects the *operator*, which the framework
  already used; it does not produce binding energies. Its value is making the
  selection *principled and input-free*, closing #2433's "promote the criterion
  into the program" — it is a conceptual/structural result, not a new prediction.
- **Watch for overclaim:** do not state "binding closed". The honest headline is
  "the confinement-operator selection is now a non-fitted topological program
  (Brunnian + crossing-minimal); binding magnitude stays research-grade
  (Subgoal-2, owner-declined)."

## Next steps (if pursued — research-scale)

1. Wire a Brunnian-3-braid enumerator (SnapPy or hand-rolled crossing-number
   enumeration) to *prove* the crossing-minimal-Brunnian = Borromean uniqueness,
   replacing the literature citation with a witness.
2. Edit `confinement-operator-selection.md` to make the Brunnian constraint the
   *primary* selector and demote the `net_proton`-match to a *consistency check*
   (a content change — coordinate with the proof-editor/canonical watchers).
3. A Lean lemma: "the Markov-trace-confined 3-braid is the crossing-minimal
   Brunnian braid" as a `conjecture`/`def` with the Brunnian predicate axiomatized.

## Cross-links
- [`b3_brunnian_selection_scope.py`](../../computations/probes/b3_brunnian_selection_scope.py) — this branch's scoping probe.
- `docs/audits/2026-06-17-b3-dense-sdp-lever-closed.md` — the operator-space refutation that motivates moving to link space.
- `docs/audits/2026-06-17-delta-lambda-two-remaining-directions-closed.md` (#2433) — verdict (1) naming this direction.
- `content/quantum-observable-universe/particle-interactions/confinement-operator-selection.md` — the current net-target + tiebreak selection to be reframed.
