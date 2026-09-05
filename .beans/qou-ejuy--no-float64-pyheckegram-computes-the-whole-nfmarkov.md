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
