# A_ω normalization — reconciling the one-instanton closed form with the corpus residue dictionary (2026-07-25)

**Branch:** `claude/aomega-oneinstanton-residue-reconcile-2026-07-25`.
**Reconciles:** the one-instanton normalization brick + magnitude probe (`OneInstantonNormalization.lean`
#4246; `qbeta_5two_one_instanton_nodd_probe.py` #4260) with the corpus's established
Borel–Padé residue route (`qbeta_g3_aomega_residue_first_number.py`). **Audit only —
no new claim, no fit; a corpus-grep pointer so the closed-form-amplitude route is not
re-attempted.**

## The two routes, and how they fit

**(A) One-instanton closed form (this session, #4246/#4260).** The A_ω fibre→archimedean
map is the one-instanton imaginary part
`N_odd = 𝒜·e^{−Re𝔙/πℏ}·sin(Im𝔙/πℏ)`. #4246 proves (Lean, sorry-free) this product shape
**realizes** the `BarOddLadderShape` numerator, with the zero-log-derivative exactness a
*consequence*. #4260 tested it parameter-free (`𝒜=1`, `P=1`, `ℏ=log q`): it **supplies
the zero-crossing** the raw `Im(ι₁₃)` form lacked, but its **naive amplitude is off**
(slope 4 orders short, prefactor ~60× large).

**(B) Borel–Padé residue dictionary (established corpus route).**
`qbeta_g3_aomega_residue_first_number.py` uses the canonical resurgence dictionary

> `disc f = 2πi·r·e^{−ζ₀·N}`,  ζ₀ = ι = `𝔙/(2πi)` (Borel singularity, `= Vol/π` at `u=0`),
> amplitude `= |2πi·r|` (Padé residue of the κ_n tower).

u=0 control: pole at `Vol/π`, amplitude within a factor 5 of the GGM integer `3`. The
**deformed** leg extracts `|2πi·r̃|` at `u_sub = 0.20868 = 2 log q₀` — "the A_ω-adjacent
number the corpus has never had."

## The reconciliation (what the refine resolves)

The refine question was: *derive* the closed form's prefactor / `ℏ`-scaling (route A),
without tuning. Routes A and B answer it together:

1. **The exponent object is `ζ₀ = ι = 𝔙/(2πi)`, not `𝔙`.** Route B fixes the Borel
   singularity as `ι = 𝔙/(2πi)` (its own definition, = `Vol/π` at `u=0`). So the
   closed form's exponent should use `ι`, which is `𝔙` rotated by `1/(2πi)` — resolving
   the `Re𝔙`-vs-`Im𝔙` decay/oscillation ambiguity that route A left open. This is a
   **derived** convention (route B's, cited), not a tuned choice.

2. **The A_ω amplitude is the Padé residue `|2πi·r|`, NOT the closed-form exponential
   prefactor.** This is the crux: route A's `e^{−Re𝔙/πℏ}` is **the wrong amplitude
   object**. The derived amplitude — the one already used on the `u=0` integer-3 control
   and extracted at `u_sub` — is the **residue of the Borel transform of the measured
   κ_n tower**. So route A's parameter-free magnitude miss (#4260) is **explained**: a
   naive exponential prefactor is not the Stokes amplitude; the residue is.

3. **The structure (route A, Lean) and the amplitude (route B, residue) are
   complementary, not competing.** The one-instanton *shape* — the CS-phase `sin`
   producing a simple zero with a log-derivative-free slope (`OneInstantonNormalization.lean`,
   proved) — is the correct structural skeleton. Its *amplitude* is supplied by route
   B's residue. Neither alone is the map; together they are: **structure from A
   (Lean-proved), amplitude from B (derived residue).**

## Net (honest, no fit)

The "derived prefactor/`ℏ`-scaling" the refine sought is **already in the corpus** as the
Borel–Padé residue dictionary (route B). The one-instanton closed form's amplitude route
(route A's `e^{−Re𝔙/πℏ}`) is **superseded** for the amplitude — it is the wrong object,
and its parameter-free miss (#4260) is honestly explained by that. **No future agent
should re-attempt to close A_ω by tuning the closed-form prefactor / `ℏ`-scaling** — the
derived amplitude is the residue, and pinning it further is the residue route's job
(higher κ_n rungs / a proved Habiro element), not a closed-form fit.

The remaining open capstone (`conj:algebraic-geometric-dilog-equivalence`) is therefore:
prove the residue `|2πi·r̃|(u_sub)` equals the odd A_ω amplitude in closed form (a Habiro
/ quantum-modular identity), with the **structure** already Lean-fixed
(`OneInstantonNormalization.lean`) and the **exponent object** fixed as `ι = 𝔙/(2πi)`.
That is a sharper target than "find the normalization map" — the map is identified; only
the residue's closed form is open.
