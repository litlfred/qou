# The surviving binding object has a well-ordered expansion; the refuted one does not

**Answers the question** left explicitly open by the `c₃` audit: does
`log(tr_free/tr_atom)` — the object #6611 derived as the binding law — have a
better-ordered `ℏ_q` expansion than `Δtr = tr_free − tr_atom`, which #6611
refuted? Beans `qou-brng` / `qou-pdg9`.

**Yes, at every case measured.** And two exact structural facts fall out, one of
which independently corroborates #6611's own criticism of its replacement.

## Measured

`ℏ_q`-expansion of `log(tr_free/tr_atom)`, all six cases, exact rationals:

    case  A      L0     L1·ℏ    L2·ℏ²   |L1ℏ|/L0  |L2ℏ²|/L0
    pp    2  0.6931  −0.1982  +0.0147     28.6%      2.12%
    pn    2  0.6931   0.0000  −0.0147      0.0%      2.12%
    nn    2  0.6931  +0.1982  −0.0049     28.6%      0.71%
    T     3  1.3863  +0.1982  −0.0196     14.3%      1.42%
    3He   3  1.3863  −0.1982   0.0000     14.3%      0.00%
    4He   4  2.0794   0.0000  −0.0049      0.0%      0.24%

at `ℏ_q = 0.099081716044258508` (proton pin).

**Against `Δtr` at A = 4** (the `c₃` audit): `0.20049, 0.29350, 0.24121` — three
orders spanning a factor 1.46, no leading order at all.

So the log-ratio is **strictly ordered in every case** — each order smaller than
the last, worst case 28.6 % then 2.1 % — where the difference has no ordering.
That is a real structural difference between the object that failed as a binding
law by **1592×** and the one that works at **1.225×**.

## `L0 = (A−1)·log 2` — derivable, not merely observed

Exact on all six. It follows from the *already-proved* `c₀` structure:
`tr_free(0) = 2^{−A}` and `tr_atom(0) = 2^{1−2A}`, so

    L0 = log(2^{−A} / 2^{1−2A}) = log 2^{A−1} = (A−1)·log 2.

**Consequence for #6611's law.** `B = E₀·log(tr_free/tr_atom)` is therefore, at
leading order, **exactly linear in A with slope `E₀·log 2`** — the shape of the
volume term in the semi-empirical mass formula.

**Stated as an observation, not a derivation of the volume term.** What is shown
is that the leading term of this particular expansion is linear in A. Whether
that *is* the SEMF volume term requires matching the coefficient against
`a_V ≈ 15.8 MeV`, which is not done here and which `E₀` is independently known
to miss (#6611: "E₀ is 2.656× below the best single scale").

## `L1 = 2·(i_nn − i_pp)` — and it reproduces #6611's own defect

With `i_pp = max(Z−1,0)`, `i_nn = max(N−1,0)` — the *chain-interface* counts, not
pair counts — the first-order coefficient is **exact on all six cases**:

    case  Z  N   i_pp i_nn   predicted   actual
    pp    2  0    1    0        −2        −2
    pn    1  1    0    0         0         0
    nn    0  2    0    1        +2        +2
    T     1  2    0    1        +2        +2
    3He   2  1    1    0        −2        −2
    4He   2  2    1    1         0         0

So `L1` is **pure isospin asymmetry with no A-dependence whatsoever**.

**This independently corroborates #6611's roast of its own replacement.** That
commit records: *"the derived isospin asymmetry has the wrong sign."* Here is
the mechanism explicitly — neutron-rich means `i_nn > i_pp` means `L1 > 0` means
**more** binding, whereas the SEMF asymmetry term `−a_A(N−Z)²/A` demands less.
Reached from the expansion side rather than from the AME fit, so it is a second
independent route to the same defect.

## A correction to my own earlier claim

An earlier report in this arc stated that `L1 = 0` is "exact, not small", on the
strength of ⁴He alone, and quoted `|L2ℏ²|/L0 = 0.24 %` as *the* measure of how
well-ordered the log-ratio is.

**Both were ⁴He-specific and the first was misleading.** `L1 = 0` holds **only at
Z = N** (pn and ⁴He), where `i_nn − i_pp` cancels; it is `±2` in all four Z ≠ N
cases. The ordering range is **0.24 %–28.6 %**, not 0.24 %. The headline
conclusion survives — the log-ratio orders and `Δtr` does not — but it rests on
the whole table, not on the best case.

## Scope, and what is NOT established

- **Six cases, A ≤ 4.** Nothing here constrains A ≥ 5. `L0` and `L1` are exact
  closed forms *fitted to six points*; `L0` is additionally derived from the
  proved `c₀` structure, but `L1` is **pattern-matched, not derived**, and six
  points is a thin basis for a two-parameter form.
- **`L2` has no closed form here.** It takes `3/2, −3/2, −1/2, −2, 0, −1/2` across
  the six and no pattern was sought or found.
- **Three orders only**, and only because `d.p = 4` after the pipeline's
  precision loss.
- **Not a claim about the physics.** This is the expansion structure of a
  computational object. Whether `E₀·log(tr_free/tr_atom)` is the right binding
  law is #6611's question, and it answers it with a scale that is 2.656× off.
- **The `Δtr` comparison is at A = 4 only** — the case where `Δtr` was measured
  to three orders.

## Method

Both traces from `tr_M_series(2,2,·,P=5)` (`tf.p = ta.p = 4`), the log-ratio
expanded symbolically in `ε` and mapped to `ℏ` by `ε = h/(1−h)`, the same
substitution used and self-checked in the `c₃` work. Every coefficient is an
exact `Fraction`; `ℏ_q` weighting is mpmath at 25 dps. The A = 4 coefficients
were re-derived by hand from the printed ε-coefficients and agree, and
`Δtr(0) = 1/16 − 1/128 = 7/128` reproduces `a₀` from the `c_k` runs — a
cross-check that the two computations are looking at the same object.
