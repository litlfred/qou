# probe-d `Delta_tr` move: exact attribution (bean `qou-xj4p`)

`probe_d_dressing_is_proton_net.py` forms `B_D = E₀·net(p)·Δtr` with
`Δtr = tr_M(free) − tr_M(atom)` for the deuteron (`tr_m_atom_zn(1, 1)`). The
committed witness (computed 2026-07-04 at main `581c176f480`; its recorded
`commitSha 4dfe838c398` was rewritten by the rebase-merge) has
`Δtr = 0.59516889262234348652`. The producer on main gives `0.14704667798040846911`.
`E₀` and `net(p)` did not move: `B/(net(p)·Δtr)` is `4.18598136329447589` in both
witnesses (relative difference 5e-19). So the whole `B_cand` move is `Δtr`.

## Method

1. Worktree at `581c176f480`, same Python environment. `tr_m_atom_zn(1, 1, dps=70)`
   reproduces `0.5951688926223434865224082`, matching the witness to all 20 recorded
   digits.
2. Dumped, from that tree and from main (grouped core), the `y_λ` table (`n = 6`), both
   words, and the `χ^λ` tables. Swapped them across trees.
3. On main, `delta_tr_attribution.py` (this directory) recomputes every step from
   main's own code (convention C through
   `schur_principal_mpmath.y_lambda_at_q0_mpmath_convention_C_HISTORICAL`). It checks
   that step 0 reproduces the witness and the last step reproduces the live
   `tr_m_atom_zn`. Output: `delta-tr-attribution.witness.json`. mpmath, 70 dps, no
   float64 arithmetic.

## What the 2026-07-04 run actually computed

- `y_λ` was **convention C** (pre-2026-08-09) and came from the
  `y-lambda-at-q0.witness.json` cache. That cache was built at the **retired muon pin**
  `1.10997859555733471989…` (its `parameters.q_0`, computed 2026-06-22). The old
  accessor served the cache whenever `|q − q_parameter.Q| < 1e-12`, and
  `tr_m_atom_zn` passed `q_parameter.Q` itself (the proton pin), so the gate passed
  trivially and returned the muon-built table. Measured: the old tree's
  `y_lambda_at(6, Q)` equals convention C at the retired muon pin exactly. So the old
  run was a **layer straddle**: `y_λ` at muon, `χ^λ` at proton.
  This is the straddle AGENTS.md describes for the μ₃ Fréchet probe.
- `χ^λ` was at the 50-digit proton q₀, but the word's interface coefficients `d` were
  built from the **float64** q₀ (`d = −0.1045301493978196827` against
  `−0.1045301493978196577` now).
- The word was the **grouped** confinement core (pre-2026-09-05).

## Attribution (path: pin → convention → precision → word)

| step | Δtr after step | contribution | share of total move |
|---|---|---|---|
| old witness (C, y@retired muon, grouped, f64 `d`) | 0.59516889262234348652 | | |
| (c) word `d` float64 → 70-digit q₀ | 0.59516889262234348651 | −1.35e-20 (measured in old tree) | 3e-20 |
| (b) `y_λ` pin retired muon → proton | 0.59516889120695734626 | −1.41538614e-9 | 3.16e-9 |
| (a) Markov convention C → D | 0.55654466040443821190 | **−0.0386242308025191344** | **8.619 %** |
| word ruling grouped → alternating | 0.14704667798040846911 | **−0.409497982424029743** | **91.381 %** |

On the log scale the split is 4.80 % (convention) / 95.20 % (word).

**The attribution is complete.** The "unattributed ~7 %" is the Markov convention
change C → D (the convention-D cascade, owner ruling 2026-08-09). The pin straddle contributes 1.4e-9
and the float64 word 1.4e-20. Neither matters at the 1 % level the assertion tests.

### Candidate (b), all pins (grouped word, 70-digit `d`)

| `y_λ` pin | convention C | convention D |
|---|---|---|
| retired muon | 0.5951688926223434865089 | 0.5565446594826804243729 |
| muon, CODATA 2018 | 0.5951688926219948727577 | 0.5565446594829074560746 |
| muon, CODATA 2022 | 0.5951688926317828516267 | 0.5565446594765331191617 |
| proton | 0.5951688912069573462597 | 0.5565446604044382119048 |

The pin moves Δtr only in the 10th digit, whatever the pin.

### The path is not additive, and the "93 %" depends on it

The two big steps interact. Taken in the other order:

- word ruling under convention C: `0.5951688912 → 0.0987425429`, contribution
  **−0.4964263483**;
- convention C → D on the alternating word: `0.0987425429 → 0.1470466780`,
  contribution **+0.0483041351** (opposite sign).

So "x % word, y % convention" is a property of the path, not of the inputs. What
holds on both paths: the word ruling carries the move, and the convention step changes
`Δtr` by about 0.04 to 0.05 in absolute terms.

## What this means for the probe's 0.29 % hit

`B_cand = E₀·net(p)·Δtr` against AME, `E₀` and `net(p)` held at their live values:

| configuration | Δtr | B_cand (MeV) | vs AME |
|---|---|---|---|
| C, grouped (old) | 0.595168891 | 2.230943 | +0.287 % |
| D, grouped | 0.556544660 | 2.086163 | −6.22 % |
| C, alternating | 0.098742543 | 0.370129 | −83.36 % |
| D, alternating (live, canonical) | 0.147046678 | 0.551193 | −75.22 % |

The sub-percent hit holds in exactly one configuration: the superseded word under the
excised convention. The old run also straddled the muon and proton layers.
Either ruling alone breaks it. Under the anti-fit rule the hit was never evidence that
those inputs were right. This only records that the hit belongs to them.

## Reproduce

```bash
PYTHONPATH=tools/qou-substrate/python:tools/pyhecke/python:computations \
  python3 -u computations/probes/probe_d_dressing_is_proton_net/attribution/delta_tr_attribution.py
```

About 15 s. Exit 0 when all three checks pass.
