# Workplan refresh — the fibre leg after 794 main commits (2026-08-07)

**Tier:** coordination. No new results claimed. Owner-requested analysis of what
landed on `main` while this line was idle, and whether any of it helps.

## 1. Position check — the prior tranche is merged

Both PRs from this line are on `main`:

- **#4446** — R2-core tranche (SW/q-Laguerre identification, bar-reflection
  pushforward closed scope-(b), exact tropical transport).
- **#4507** — the `A_w` zero localization
  ([`AwZeroLocalization.lean`](../../folio/quantum-observable-universe/lean/QOU/Archimedean/AwZeroLocalization.lean)
  verified present on `main`), plus the F-vs-K survey.

The working branch was therefore stale *and* redundant; it has been restarted
from `origin/main`. Nothing was lost.

## 2. Chain status (unchanged by main's landings)

| Step | State |
|---|---|
| Archimedean leg | closed |
| Family identification (SW ⊛ Jackson; one-sided = Moak q-Laguerre) | exact |
| E-transport of tropical **classes** | exact, Lean |
| SW core: extremal ↔ tropical | **proved** (`A_w`, reaches the substrate pin, `n₀ = 135`) |
| Balanced: extremal ↔ tropical | **open** — partial only, see §4 |
| Friedrichs vs Krein selection | **open**, and not addressed by any class-level result |

The last row is the conjecture's actual closing question. F and K occupy
*complementary sublattices of the same* `u ≡ 1` class, so no lattice/class
argument can separate them — recorded in `qou-r4ya` after that bean's own title
was corrected for overstating this.

## 3. Does anything on `main` help? — mostly no, with one mild positive

794 commits, clustered: Lean formalization closure (the largest block — "15
axioms proved, 79 sorries closed"), Δ_λ probes and negatives, the eightfold-way
tranche, Kashaev/volume-conjecture instances, na-Stokes binding work.

Checked specifically:

- **My files are untouched.** `git log HEAD..origin/main` over
  `QOU/Archimedean/`, the conjecture block, and the `ksel2id_*` probes returns
  nothing relevant. No collision, no help.
- **Six commits mention the domain** (moment / Stieltjes / Wigert / extension /
  Nevanlinna / Friedrichs / Krein). Four are this line's own merged work. The
  other two are `lean(covariance): binomial-square moment sums` — a *different*
  moment computation, part of the (TAIL) covariance derivation, with no bearing
  on the balanced moment problem — and a Δ_λ two-moment cross-check.
- **The one "kernel" commit is a different kernel.**
  `lean+audit(na-Stokes leg): brane resummation is a convergent affine fixed
  point; ℏ² kernel undershoots binding 450×` consumes the ℏ²-damped brane tower,
  not the balanced representing kernel. It is a binding-front result (a large
  honest negative), not the F-vs-K discriminator.

**The mild positive.** The F-vs-K survey named the decisive test as: *sweep the
corpus for a non-moment consumer of the balanced kernel — an empty result puts
a determinacy-of-consumption theorem in reach; a hit is the discriminator.*
794 commits later that sweep is **still empty**. That is weak evidence, not a
proof, but it is evidence in the direction the survey predicted: it strengthens
**P4 (non-selection)** as the best-supported reading, and makes
"determinacy-of-consumption" the shape of a positive result rather than a shrug.

**The honest read of the whole line.** This remains R2-core. Under the standing
owner ruling `1/(8π)` stays phase-4 and nothing wires, so closing the fibre leg
completely still moves no observable; L2 stays where it is. The value is
structural.

## 4. The orphaned balanced-theta-limit attempt — incomplete, preserved, not cited

The agent attacking `qou-r4ya` (run the `A_w` theta-limit machinery on the
balanced D-function) terminated on a session limit mid-debug, reporting
*"B4's stability test was mis-specified."* Its three artifacts are preserved
under a prominent INCOMPLETE banner and are **not** cited as results anywhere:

- the audit carries a literal `PLACEHOLDER_VERDICT` and no verdict table;
- its Lean file is **not** registered in `QOU.lean`;
- no exit-0 claim is made for its probe.

It claims substantially more than a fragment. Its title asserts that the
`E`-shifted recentring absorbs `E` exactly (under
`d_j = d_0(−1)^j E^{−j} w^{j²} g_j`), that the theta limit is the **same**
Jacobi triple product as the SW core's, and that the Rouché transfer splits into
a sharp route that does not carry and a crude route that does. **If those hold
they would largely settle the balanced leg** — which is exactly why they must
not be cited before checking: the verdict section was never written, and the
block that tests stability is the one the agent called mis-specified. Treat the
whole document, title included, as an unverified lead.

## 5. Prioritized queue

1. **Finish or abandon `qou-r4ya` deliberately.** Re-run the balanced
   theta-limit with B4 re-specified. Either the limit transfers (balanced class
   derived) or the Jackson edge obstructs the triple-product structure — both
   are publishable; the current half-state is not.
2. **P4 as a positive result** (`qou-f6sm` follow-on). Formalize
   determinacy-of-consumption: if every corpus consumer of the kernel is a
   moment functional, the F/K ambiguity is invisible to the framework and
   non-selection is the *answer*, not a gap. The sweep in §3 is the first
   input.
3. **Do not work** `qou-jbo8` / `qou-x1rm`. Both optional Mathlib-PR-sized
   infra, both cost-corrected upward, neither on any critical path.
4. **Pivot candidate, unchanged:** the binding front. Main's landings there are
   mostly negatives (Δ_λ two-moment cross-check fails; deuteron naive-z dead
   across A; ℏ² kernel undershoots 450×), which narrow the front without
   supplying a tool. The tropical/Newton-polygon lens that worked here remains
   the distinct angle worth trying, and B2 (angle-structure LP ↔ SDP duals)
   remains unclaimed and fit-free.

## 6. Cross-references

- [`2026-08-01-ksel2id-tropical-transport.md`](../audits/2026-08-01-ksel2id-tropical-transport.md)
- [`2026-08-01-awzero-asymptotics.md`](../audits/2026-08-01-awzero-asymptotics.md)
- [`2026-08-01-fvk-selection-framing.md`](../audits/2026-08-01-fvk-selection-framing.md)
- Conjecture block: [`schwinger-measure-computational-time.md`](../../folio/quantum-observable-universe/predicted-spectra/schwinger-measure-computational-time.md)
