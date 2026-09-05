---
# qou-ejuy
title: 'NO-FLOAT64: pyhecke.gram computes the whole NF/Markov-trace path in float64 (z, h, TR_M are Python floats)'
status: todo
type: task
created_at: 2026-09-05T06:41:44Z
updated_at: 2026-09-05T06:41:44Z
---


Found while excising the 391 raw float64 fields from `hadron_knot_table`'s
witness path (bean `qou-uiut`). Those fields were the SYMPTOM; this is where
they come from.

## Measured

    $ cd computations && python3 -c "from pyhecke.gram import TR_M, z, h; ..."
    z type: float    0.6126880371464652
    h type: float    0.20906029879563937
    TR_M dtype: float64
    TR_M[1]: np.float64(0.6126880371464652)

`tools/pyhecke/python/pyhecke/gram.py`:

    z = q0 ** 3 / (q0 ** 2 + 1)                                   # line 199
    TR_M = np.array([1.0, z, z, z ** 2, z ** 2, h * z ** 2 + z])  # line 220

    def nf_tr(nf):  return sum(nf[i] * TR_M[i] for i in range(6))
    def nf_net(nf): return sum(nf)

So the Markov trace of every NF element is a float64 dot product against a
float64 basis vector, and `z`, `h` and `q0` in that module are Python floats
throughout. This is not a serialization defect that a `fmt` call fixes — the
VALUES have ~17 significant digits before anything is written.

## How it surfaced

Converting `hadron_knot_table`'s row builder from `round(float(x), 12)` to
`fmt(x)` made it visible immediately, because `fmt` short-circuits a non-mpf
to `str(value)`:

    tr_M       str  0.6293284243136998                    <- 16 digits: float64
    net        str  1.2080837755920566                    <- 16 digits: float64
    nf['γ']    str  -0.09218806086752263                  <- 17 digits: float64
    ln_abs_tr  str  -0.46310202132421752246343384577958…  <- 53 digits

The last line is the tell. `ln_abs_tr` is `mp.log(abs(tr))`, and `mp.log`
promotes its float64 argument to mpf and returns 60 genuine digits — of the
logarithm of a number that only HAS 17. Digits 18-60 describe the binary64
rounding of `tr`, not the physics. That is manufactured precision, and the
`round(..., 12)` this replaced had been accidentally hiding it.

Capped at `dps=17` in `hadron_knot_table` for now, with a comment pointing
here. **When this bean lands, drop that override** — the honest width is the
full one once the input deserves it.

## Blast radius — DO NOT patch this casually

`pyhecke` is a shared library under `tools/`, not a producer. Changing `z`,
`h` and `TR_M` to mpf changes the value of every Markov trace in the corpus,
so it moves published numbers across many witnesses at once. It also has a
convention gate — `scripts/build-pyhecke-native.sh` checks
`markov_z(q0)` against the registry to 1e-15 on the "f64 path", so the native
wheel and the Python module are currently expected to agree AS float64.

Scope, in order:

1. Establish whether `pyhecke.gram` is meant to be the f64 fast path with the
   MPFR kernel as the precise one. If so, the defect is not gram.py itself but
   that `hadron_knot_table` reads its trace from the f64 path while taking
   `B_MeV` from the MPFR pipeline — a witness mixing two precisions.
2. If gram.py is meant to be precise: convert `z`, `h`, `TR_M` and the `nf_*`
   helpers to mpf, and re-derive the convention gate's tolerance, which is
   written for f64.
3. Either way, `TR_M` as `np.array` forces float64 regardless of what `z` and
   `h` become — an object-dtype array or a plain tuple is required.
4. Identify the consumers before changing anything. `nf_tr` / `nf_net` are
   library entry points; this is the "find the callers first" discipline that
   `qou-fop2` needed and did not have.

## 2026-09-05 — the gating question is ANSWERED, and it is not what this bean assumed

Scope item 1 asked whether `pyhecke.gram` is meant to be the f64 fast path.
**It is, explicitly, and it already ships the mpf counterparts.** So this bean
is a CONSUMER fix, not a library fix, and the title above is wrong in its
implication that gram.py is defective.

`gram.py` carries this immediately below the import (bean `qou-jtbo`):

    ⚠ `q0`, `qi`, `h` above are the **float64** path. They are deliberately
    bit-stable — `constants.py` says "Don't change them — downstream f64
    callers depend on stability" — so they are correct for existing witness
    scripts and must not be converted.
    ...
    **The mpf counterparts already exist in this module** — use them:
        h_mp(dps=50)   z_mp(dps=50)   tr_m_mp(dps=50)   gram_matrix_mp(dps=50)

So converting `z`, `h` and `TR_M` — scope item 2 as originally written —
would be **wrong**, and would break the f64 callers the module promises
stability to. Struck.

### The full mp path that already exists

    pyhecke.gram    z_mp, h_mp, tr_m_mp, hm_mp, _nf_of_word_mp,
                    gram_matrix_mp, radical_mp, gram_inverse_mp,
                    gram_quotient_solve_mp
    pyhecke.atom    build_nucleon_nf_mp(quarks, dps=50)
    computations/compound_shift_nf.py:189
                    build_atom_nf_mp(Z, N, dps=50)

### So the defect is where scope item 1 guessed

`hadron_knot_table` imports `build_atom_nf`, `nf_tr`, `nf_net` (f64) and
`check_frobenius` (f64 `G @ x`), while taking `B_MeV` from the MPFR kernel —
and publishes both in one row. That is a witness mixing two precisions, and it
is also the whole of `qou-3uvs`: the LP_stable predicate's `-1e-10` tolerance
sits 25 orders below one float64 ulp at fe56 precisely because `G @ x` is f64.
Moving the table to `build_atom_nf_mp` + `tr_m_mp` + `gram_matrix_mp` fixes
both beans at once.

### Not done in this session, deliberately

The `qou-uiut` regeneration was in flight when this was established. Swapping
an unverified `build_atom_nf_mp` for `build_atom_nf` mid-run would have meant
restarting a 4.6-hour job on the assumption that the two agree — and they need
to be shown to agree first, on the light atoms, where `build_atom_nf` is cheap
and trustworthy. The current run still lands a strictly better artifact than
what is committed: faithful serialization, `B_MeV` at 60 real digits, and `Gx`
recorded so the stability verdicts become auditable.

### Revised scope

1. [x] Establish whether gram.py is the f64 fast path. IT IS.
2. [ ] ~~Convert z, h, TR_M to mpf~~ — STRUCK. Would break the f64 callers
       the module guarantees stability to.
3. [x] Show `build_atom_nf_mp(Z, N, 50)` agrees with `build_atom_nf(Z, N)`.
       **IT DID NOT, and the disagreement WAS the finding.** 8.5e-5 (deuterium)
       to 7.7e-4 (li6) — twelve orders above float64 noise, so a different
       computation rather than a precision difference.

       Cause: for the INTER-nucleon p-n crossing the "mirror" used `-h/2`, the
       superseded `strict_averaged` convention, where the canonical builder
       uses the colour-weighted `D_PN = pn_interface_offset(q0)`:

           D_PN  = -0.10445824776972631
           -h/2  = -0.10453014939781968     rel 6.88e-4

       Its docstring claimed "Mirror of hecke_core.build_atom_nf — exact same
       generator sequence". It had fallen behind the function it mirrors: the
       same divergence-between-copies class as the `.dot` and `a_rho` defects,
       and as the vendored qou-mass drift under `qou-qe81`.

       FIXED by calling `pn_interface_offset(q0)`, which is type-generic and
       returns an mpf. The INTRA-nucleon ud crossings stay literal `-h/2` —
       the canonical builder writes them that way too, and only the
       inter-nucleon site is colour-weighted. After, over six atoms including
       c12: `max|nf f64-mp|` 4.0e-16..4.5e-15, `rel(tr)` 1.9e-16..1.2e-15,
       i.e. differing only by the f64 side's own rounding.

       Had this step been skipped, moving `hadron_knot_table` to the mp path
       would have shifted the physics by 7e-4 while looking like a clean
       NO-FLOAT64 upgrade.
4. [x] Moved. `build_atom_nf_mp` / `build_nucleon_nf_mp` for the NF,
       `tr_m_mp(50)` for the trace, and a local `check_frobenius_mp` over
       `gram_matrix_mp(50)` (local, not in the library: the f64
       `check_frobenius` is on the bit-stable path other callers rely on).
       The `dps=17` cap on `ln_abs_tr` is dropped and the `float()` in the `Gx`
       serialization is gone. Measured on deuterium, every field now carries 60
       real digits:

           tr_M       0.404396338473143412297181623713549507554654248186911…
           net        1.15453793492571046672735243477077542992790931074548…
           B_MeV      -7.2711025986821821719155043668348962979451059325080…
           Gx[0]      0.404396338473143412297181623713549507554654248186911…

       Sanity: the mp `tr_M` agrees with the committed f64 value to ~9 digits
       (0.404396338473… vs 0.404396337968…, ~5e-10 apart) — the f64 path's
       accumulated rounding through the NF multiplications, which is exactly
       what this removes.
5. [ ] Re-run and diff. tr_M, net, nf and every LP_stable verdict move; that
       is the point, and `qou-3uvs`'s noise floor goes away with it.
6. [ ] Find the OTHER f64-path consumers before declaring this done. `nf_tr`
       and `check_frobenius` are library entry points and this table is
       unlikely to be the only caller mixing precisions.
