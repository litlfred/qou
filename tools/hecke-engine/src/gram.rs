//! Gram matrix on the NF basis of H_3(q) — Rust implementation.
//!
//! Mirrors `pyhecke.gram` (see
//! `tools/pyhecke/python/pyhecke/gram.py`). Same NF basis, same Hecke
//! reduction rules.
//!
//! # Convention D, correct Markov trace, singular form — read this first
//!
//! Both long-standing divergences from the Python mirror are RESOLVED as of
//! 2026-08-15:
//!
//! **1. `TR_M[5]` is now `h·z² + z`**, matching `pyhecke.gram.TR_M`. It was
//! `z³` here from before 2026-05-19 — the bug
//! `docs/audits/2026-05-19-trm5-markov-bug.md` fixed in Python and never
//! ported. `h·z² + z` is the correct Markov trace of `e⁻ = σ₀σ₁σ₀`
//! (cyclicity plus `σ₀² = h·σ₀ + 1`).
//!
//! **2. The Gram is therefore SINGULAR**, and that is correct, not a defect.
//! Under convention D with the right trace the 6×6 Markov–Gram form is
//! degenerate — see
//! `folio/quantum-observable-universe/lean/QOU/QBeta/GramSignature.lean`.
//! Note that file's own retraction (commit `748ba9b1`): its "Lorentzian /
//! signature (4,1)" reading is WITHDRAWN — under the correct `*`-pairing
//! (`T_w* = T_{w⁻¹}`) the form is positive semidefinite, `(5,0,1)`. What
//! survives both readings, and is all this note relies on, is that there is
//! exactly ONE null direction.
//!
//! **So there is no 6×6 inverse, and [`gram_inverse`] is gone.** Use
//! [`gram_quotient_inverse`] — the Moore–Penrose inverse on `H_3(q)/rad` —
//! and [`gram_radical`] for the null direction. `gram_inverse` was NOT
//! repointed at the pseudoinverse: they differ exactly on the radical, and
//! silently handing a caller a different object under a trusted name is how
//! a wrong number keeps circulating.
//!
//! The scale of the change, measured: `TR_M[5]` moves +200.5 % (0.2300 →
//! 0.6912), 19 of 36 Gram entries move, rank 6 → 5, and `‖G⁺ − G⁻¹‖` is
//! 73.3 % relative. Downstream numbers derived from the old inverse move
//! substantially — this was a re-derivation, not a patch.
//!
//! Public API:
//!
//! * [`gram_matrix`] — 6×6 Gram at an arbitrary `q > 1`.
//! * [`gram_quotient_inverse`] — inverse on `H_3(q)/rad` (the form is
//!   singular, so no 6×6 inverse exists).
//! * [`gram_radical`] — the null direction, in closed form.
//! * [`GramCertificate`] — serde-serializable record matching the
//!   JSON shape used by `pyhecke.certificate`.
//! * CLI entry via `cargo run --bin hecke-gram`.

use serde::{Deserialize, Serialize};

/// NF basis of H_3(q): 1, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀.
pub const NF_BASIS: [&[u8]; 6] = [
    &[],
    &[0],
    &[1],
    &[0, 1],
    &[1, 0],
    &[0, 1, 0],
];

pub const NF_NAMES: [&str; 6] = ["gamma", "sigma_0", "sigma_1", "L_plus", "L_minus", "e_minus"];

/// Default substrate parameter q_0 — the **PROTON** pin, `m_p/m_e`.
///
/// Matches `q_parameter.Q` / `qou_substrate.constants.Q`, which is what
/// `pyhecke.gram` reads.
///
/// RE-PINNED 2026-08-15 (owner decision, bean `qou-m7py`) from the MUON pin
/// `1.1099785955541805`, 11.54 ppb away. AGENTS.md's owner directive of
/// 2026-08-07 makes the experimental/proton pin the default for all
/// production compute; this constant was the last muon-pinned production
/// value in the crate. The prior note here correctly declined to change it
/// as a side effect of the convention migration — it is an owner decision
/// because it moves every certificate the engine emits — so it was taken
/// as one, separately.
///
/// Effect: `markov_z(Q_0)` moves 0.6126880505455892 -> 0.6126880371464652,
/// which is now EXACTLY the `pyhecke.gram.z` value. The crate and the Python
/// mirror no longer straddle the ideal/experimental layer boundary.
///
/// Scope note — CORRECTED. An earlier version of this note claimed this was
/// "the only *production* muon literal in the crate", counting only the
/// `1.1099785955541805` spelling. It is not: five live binaries hardcode the
/// 5-significant-digit `1.10998`, which is 1277 ppb from this anchor — a
/// hundred times further off than the re-pin the note was about, and the
/// distance `provenance::classify_pin` labels `"truncated-5-digit"`.
///
/// Still open, each feeding real compute rather than a diagnostic, so each
/// needs its output re-verified rather than a blind substitution:
///
/// | site | reaches |
/// |---|---|
/// | `bin/v14_hapower.rs:309` | `ha_val = q − 1/q`, and `t = √q` |
/// | `bin/v6.rs:484` | `Engine::new(Q0)` |
/// | `bin/v8.rs:682` | `t0_val`, and the printed report |
/// | `bin/h9_beta.rs:376` | the β-decay reduction |
/// | `main.rs:370` | `HeckeEngine::new(...)` |
///
/// Fixed here: `bin/v9.rs:888`, whose value reached only a stderr jet-bundle
/// diagnostic — no certificate content moved. The `src/archive/v2..v7` copies
/// are frozen history and stay as they are.
///
/// The genuinely-out-of-scope occurrences remain `rational_round`,
/// `precision_scalar` and `laurent_poly_q`: test inputs exercising rounding
/// and precision machinery, not the substrate anchor, with tolerances (down
/// to 1e-4) orders of magnitude larger than the 1.15e-8 re-pin.
pub const Q_0: f64 = 1.1099785827513808;

/// z = q³/(q² + 1) — Markov closure parameter, **trace convention D**
/// (SU(2)/Temperley–Lieb, Jones).
///
/// Owner ruling 2026-08-09 excised convention C (`z = 1/(q^{1/2}+q^{-1/2})`),
/// which this function carried until then. Registry:
/// `docs/coordination/trace-convention-registry.md`. This symbol is
/// re-exported through all nine language bindings (pyhecke-native, wasm,
/// node, c, jvm, r, julia, gap, octave) and drives [`trace_weights`] and the
/// `v_std` quark-volume channel, so a revert here is a nine-binding change.
///
/// Incidental precision note: D is a rational function of `q`, so this no
/// longer calls `sqrt` at all — two correctly-rounded transcendental ops
/// leave the path. The engine as a whole remains f64 (`Poly`, `[[f64; 6]; 6]`,
/// `Q_0`); that is unchanged here and is tracked separately.
#[inline]
pub fn markov_z(q: f64) -> f64 {
    q * q * q / (q * q + 1.0)
}

/// h = q - q^{-1} — the Hecke relation coefficient.
#[inline]
pub fn hecke_h(q: f64) -> f64 {
    q - 1.0 / q
}

/// Markov-trace weights on the 6-element NF basis (convention D).
///
/// `TR_M[5] = h·z² + z` — the correct Markov trace of `e⁻ = σ₀σ₁σ₀`, matching
/// `pyhecke.gram.TR_M`. This entry was `z³` until 2026-08-15, the
/// pre-2026-05-19 bug that was fixed in Python and never ported here.
///
/// Correcting it makes [`gram_matrix`] SINGULAR — see the module note. That
/// is the mathematics, not a regression.
pub fn trace_weights(q: f64) -> [f64; 6] {
    let z = markov_z(q);
    let h = hecke_h(q);
    [1.0, z, z, z * z, z * z, h * z * z + z]
}

/// Markov-trace weights with the CORRECT `TR_M[5] = h·z² + z`.
///
/// Matches `pyhecke.gram.TR_M` exactly. `e⁻ = σ₀σ₁σ₀` reduces by cyclicity plus
/// `σ₀² = h·σ₀ + 1`; `z³` (in [`trace_weights`]) is the pre-2026-05-19 bug.
///
/// Added alongside — rather than in place of — the buggy version so the
/// correct object is available, tested, and verifiable NOW, while the
/// user-visible switch stays a single gated line. Nothing in the shipped
/// pipeline calls this yet.
pub fn trace_weights_markov(q: f64) -> [f64; 6] {
    // Now identical to `trace_weights` — kept as a named alias because it is
    // what the 2026-08-15 additive commit introduced and what several tests
    // and external callers reference. Delete once those are retargeted.
    trace_weights(q)
}

// ─── Word representation + Hecke reduction ───────────────────────────

type Word = Vec<u8>;
type Poly = rustc_hash::FxHashMap<Word, f64>;

fn word_key(w: &[u8]) -> Word {
    w.to_vec()
}

fn poly_from(basis_idx: usize) -> Poly {
    let mut p: Poly = Default::default();
    p.insert(word_key(NF_BASIS[basis_idx]), 1.0);
    p
}

/// Multiply two polynomial representations (concatenate letters).
fn mul_polys(a: &Poly, b: &Poly) -> Poly {
    let mut r: Poly = Default::default();
    for (w1, c1) in a {
        for (w2, c2) in b {
            let mut w = w1.clone();
            w.extend_from_slice(w2);
            *r.entry(w).or_insert(0.0) += c1 * c2;
        }
    }
    r.retain(|_, v| v.abs() > 1e-15);
    r
}

/// Apply Hecke reductions until the polynomial is in NF.
///
/// Two rules:
///   σ_i σ_i  →  h σ_i + 1
///   σ_0 σ_1 σ_0  ↔  σ_1 σ_0 σ_1      (braid relation, canonical form)
///
/// The canonical form we keep matches the Python NF_BASIS, so any word
/// whose reduction lands on that basis stabilises after finitely many
/// rewrites.
fn reduce_nf(mut terms: Poly, h: f64) -> Poly {
    loop {
        let mut new_terms: Poly = Default::default();
        let mut changed = false;
        for (word, coeff) in &terms {
            if coeff.abs() < 1e-15 {
                continue;
            }
            let mut done = false;

            // Rule 1: σ_i σ_i = h σ_i + 1
            for p in 0..word.len().saturating_sub(1) {
                if word[p] == word[p + 1] {
                    let pre = &word[..p];
                    let suf = &word[p + 2..];
                    let mut w1: Word = pre.to_vec();
                    w1.push(word[p]);
                    w1.extend_from_slice(suf);
                    *new_terms.entry(w1).or_insert(0.0) += coeff * h;
                    let mut w2: Word = pre.to_vec();
                    w2.extend_from_slice(suf);
                    *new_terms.entry(w2).or_insert(0.0) += coeff;
                    changed = true;
                    done = true;
                    break;
                }
            }
            if done {
                continue;
            }

            // Rule 2: braid-commute to canonical form.
            // σ_a σ_b σ_a (a != b) → σ_b σ_a σ_b iff (b, a, b) < (a, b, a)
            for p in 0..word.len().saturating_sub(2) {
                let a = word[p];
                let b = word[p + 1];
                let c = word[p + 2];
                if a == c && a.abs_diff(b) == 1 {
                    let candidate = [b, a, b];
                    let original = [a, b, a];
                    if candidate < original {
                        let mut nw: Word = word[..p].to_vec();
                        nw.extend_from_slice(&candidate);
                        nw.extend_from_slice(&word[p + 3..]);
                        *new_terms.entry(nw).or_insert(0.0) += coeff;
                        changed = true;
                        done = true;
                        break;
                    }
                }
            }
            if !done {
                *new_terms.entry(word.clone()).or_insert(0.0) += coeff;
            }
        }
        new_terms.retain(|_, v| v.abs() > 1e-15);
        terms = new_terms;
        if !changed {
            break;
        }
    }
    terms
}

// ─── Gram matrix ─────────────────────────────────────────────────────

/// Compute the 6×6 Gram matrix on the NF basis at a given `q`.
///
/// `G[i, j] = tr_M(b_i · b_j)` where `b_k = NF_BASIS[k]` and
/// `tr_M` is the Markov trace extended linearly.
pub fn gram_matrix(q: f64) -> [[f64; 6]; 6] {
    gram_from_weights(q, &trace_weights(q))
}

/// Gram matrix built from an explicit weight vector.
///
/// Factored out of [`gram_matrix`] so the same NF reduction can be driven by
/// either the legacy [`trace_weights`] (`z³`) or the correct
/// [`trace_weights_markov`] (`h·z² + z`) without duplicating the loop. This is
/// the whole mechanical content of the pending TR_M[5] repair: once the owner
/// decision below is taken, `gram_matrix` repoints to `trace_weights_markov`
/// and nothing else in this function changes.
fn gram_from_weights(q: f64, tr_m: &[f64; 6]) -> [[f64; 6]; 6] {
    let h = hecke_h(q);
    let mut g = [[0.0f64; 6]; 6];
    for i in 0..6 {
        for j in 0..6 {
            let prod = mul_polys(&poly_from(i), &poly_from(j));
            let nf = reduce_nf(prod, h);
            let mut acc = 0.0;
            for (k, basis_word) in NF_BASIS.iter().enumerate() {
                if let Some(c) = nf.get(*basis_word) {
                    acc += c * tr_m[k];
                }
            }
            g[i][j] = acc;
        }
    }
    g
}

/// Gram matrix under the CORRECT Markov trace ([`trace_weights_markov`]).
///
/// SINGULAR by construction — see [`gram_radical`]. Use
/// [`gram_quotient_inverse`] rather than [`gram_inverse`] with this.
pub fn gram_matrix_markov(q: f64) -> [[f64; 6]; 6] {
    // Now identical to `gram_matrix`; see `trace_weights_markov`.
    gram_matrix(q)
}

/// The radical of the Markov trace form under convention D, in closed form.
///
/// `v_i = (-1/q)^len(w_i)` over [`NF_BASIS`] — the three-strand
/// q-antisymmetriser `Σ_w (-1/q)^ℓ(w) T_w`. Mirrors `pyhecke.gram.RADICAL`
/// exactly, including normalisation (it is NOT a unit vector).
///
/// This is a null direction of [`gram_matrix_markov`], NOT of the legacy
/// [`gram_matrix`] — the `z³` bug is precisely what makes the legacy form
/// non-singular. Established exactly over ℚ (no floating point) at three
/// independent rational `q` by
/// `computations/probes/gram_radical_exact_probe.py`.
pub fn gram_radical(q: f64) -> [f64; 6] {
    let mut v = [0.0f64; 6];
    for (i, w) in NF_BASIS.iter().enumerate() {
        v[i] = (-1.0 / q).powi(w.len() as i32);
    }
    v
}

/// Inverse of the Markov trace form on the quotient `H_3(q)/rad`.
///
/// The Moore–Penrose pseudoinverse of [`gram_matrix_markov`], and the honest
/// replacement for [`gram_inverse`] under convention D: that form is singular,
/// so a 6×6 inverse does not exist and Gauss–Jordan on it either panics or
/// inverts rounding noise.
///
/// Computed by the rank-one shift rather than a general SVD, which is exact
/// here because the kernel is known in closed form and is one-dimensional. For
/// symmetric `G` with unit kernel vector `u`,
///
/// ```text
///     (G + α u uᵀ)⁻¹ − (1/α) u uᵀ  =  G⁺        for any α ≠ 0
/// ```
///
/// since the shift moves the single zero eigenvalue to `α`, leaving the other
/// five eigenpairs untouched, and the subtraction removes the `u` direction
/// again. `G` is symmetric by cyclicity of the trace
/// (`tr_M(b_i b_j) = tr_M(b_j b_i)`), which is what licenses this. The result
/// agrees with `numpy.linalg.pinv` — pinned in the tests.
///
/// `α` is taken as the mean absolute diagonal entry so the shifted matrix is
/// conditioned like `G` itself, rather than a hardcoded constant that would be
/// badly scaled at extreme `q`.
pub fn gram_quotient_inverse(q: f64) -> [[f64; 6]; 6] {
    let g = gram_matrix_markov(q);

    // Unit kernel vector.
    let r = gram_radical(q);
    let norm = r.iter().map(|x| x * x).sum::<f64>().sqrt();
    let u: Vec<f64> = r.iter().map(|x| x / norm).collect();

    let alpha = (0..6).map(|i| g[i][i].abs()).sum::<f64>() / 6.0;

    let mut shifted = g;
    for i in 0..6 {
        for j in 0..6 {
            shifted[i][j] += alpha * u[i] * u[j];
        }
    }

    let mut inv = invert_6x6(&shifted)
        .expect("rank-one shift of the Markov Gram must be invertible");
    for i in 0..6 {
        for j in 0..6 {
            inv[i][j] -= u[i] * u[j] / alpha;
        }
    }
    inv
}

// `gram_inverse` is REMOVED (2026-08-15), not deprecated and not repointed.
//
// With the correct `TR_M[5] = h·z² + z` the Markov-Gram form is singular, so
// the object this function named does not exist. It previously ended
// `.expect("Gram matrix is singular")`, i.e. it would now PANIC on every
// call — across all nine language bindings — which is the one outcome worse
// than removing it, because it converts a type error into a runtime crash in
// a library.
//
// It was deliberately NOT rebound to `gram_quotient_inverse`. The two differ
// exactly on the radical, which is the entire content of this change; handing
// a caller a different matrix under a name they already trust is how a wrong
// number keeps circulating. A caller asking for an inverse must now see that
// there isn't one and choose explicitly.
//
// Replacement: [`gram_quotient_inverse`] (Moore-Penrose on `H_3(q)/rad`) and
// [`gram_radical`] (the null direction).

fn invert_6x6(a: &[[f64; 6]; 6]) -> Option<[[f64; 6]; 6]> {
    // Augmented matrix [A | I].
    let mut m = [[0.0f64; 12]; 6];
    for i in 0..6 {
        for j in 0..6 {
            m[i][j] = a[i][j];
        }
        m[i][6 + i] = 1.0;
    }
    for i in 0..6 {
        // Partial pivot
        let mut best = i;
        for r in i + 1..6 {
            if m[r][i].abs() > m[best][i].abs() {
                best = r;
            }
        }
        if m[best][i].abs() < 1e-15 {
            return None;
        }
        m.swap(i, best);
        let pivot = m[i][i];
        for j in 0..12 {
            m[i][j] /= pivot;
        }
        for r in 0..6 {
            if r == i {
                continue;
            }
            let factor = m[r][i];
            if factor == 0.0 {
                continue;
            }
            for j in 0..12 {
                m[r][j] -= factor * m[i][j];
            }
        }
    }
    let mut inv = [[0.0f64; 6]; 6];
    for i in 0..6 {
        for j in 0..6 {
            inv[i][j] = m[i][6 + j];
        }
    }
    Some(inv)
}

// ─── Temperley–Lieb quotient ─────────────────────────────────────────

/// Indices into [`NF_BASIS`] spanning the Temperley–Lieb quotient at `n = 3`.
///
/// Everything except index 5, `e⁻ = σ₀σ₁σ₀`. That word is the longest element
/// of `S₃`, whose permutation `(3,2,1)` is the unique 321 pattern there, and
/// the TL quotient is spanned by the 321-avoiding (equivalently, fully
/// commutative) classes — `Catalan(3) = 5` of them.
///
/// `pyhecke.tl.tl_basis_words(3)` lists the same five in a different order,
/// `((), σ₁, σ₀, σ₀σ₁, σ₁σ₀)`, swapping positions 1 and 2 relative to
/// [`NF_BASIS`]. The Gram matrix happens to be invariant under exactly that
/// swap, so both orders give the same matrix — verified against Python's
/// literal entries in `tl_gram_matches_python_at_q0`, not assumed. Do not
/// carry the coincidence to `n ≥ 4`.
pub const TL_BASIS_INDICES: [usize; 5] = [0, 1, 2, 3, 4];

/// The Markov trace form restricted to the Temperley–Lieb quotient, `5×5`.
///
/// At `n = 3` this is exactly the principal submatrix of
/// [`gram_matrix_markov`] on [`TL_BASIS_INDICES`] — stated plainly because
/// that is what it is, and because it is what makes `n ≥ 4` a different job:
/// there the quotient is not obtained by deleting one basis element.
/// Cross-checked against `pyhecke.tl.tl_gram(3, q)` to `0.0` difference in
/// exact `ℚ(q)` arithmetic on the Python side.
///
/// Unlike the full `6×6` form this one is **non-singular for every real
/// `q > 0`**, so it has a genuine inverse — see [`gram_tl_inverse`]. That is
/// scope-(b) structural, resting on the closed form established in
/// `computations/qbeta/tl3_gram_nonsingular_probe.py` (PR #5572):
///
/// ```text
///     det G_TL = −(q⁴+1)(q²−q+1)⁴(q²+q+1)⁴ / (q²+1)¹⁰
/// ```
///
/// whose numerator has no real roots.
pub fn gram_matrix_tl(q: f64) -> [[f64; 5]; 5] {
    let g = gram_matrix_markov(q);
    let mut out = [[0.0f64; 5]; 5];
    for (a, &i) in TL_BASIS_INDICES.iter().enumerate() {
        for (b, &j) in TL_BASIS_INDICES.iter().enumerate() {
            out[a][b] = g[i][j];
        }
    }
    out
}

/// The genuine inverse of [`gram_matrix_tl`] — not a pseudoinverse.
///
/// This is the difference that motivates the quotient at all.
/// [`gram_quotient_inverse`] is a Moore–Penrose pseudoinverse of the singular
/// `6×6` form: correct, but an identity only *on* the quotient. Concretely
/// `G · G⁺` is the projector onto the rank-5 range, so
/// `‖G · G⁺ − I‖_F = √(corank) = 1` — right, and not a failure, but not an
/// identity on all of `H₃(q)`. Here `G_TL · G_TL⁻¹ = I` outright.
///
/// (The `1.64` figure recorded against `G_INV` in this repository belongs to
/// the *deleted* float64 `np.linalg.inv`, a different object; do not read it
/// as the pseudoinverse's residual.)
///
/// Returns `None` only if the `5×5` solve hits a zero pivot, which the
/// determinant above forbids for real `q > 0`; a caller seeing `None` has
/// passed a `q` outside that range.
pub fn gram_tl_inverse(q: f64) -> Option<[[f64; 5]; 5]> {
    invert_5x5(&gram_matrix_tl(q))
}

/// Determinant of the TL quotient form, by the same LU the inverse uses.
pub fn det_gram_tl(q: f64) -> f64 {
    det_5x5(&gram_matrix_tl(q))
}

/// Closed-form determinant of the TL quotient form (PR #5572).
///
/// `−(q⁴+1)(q²−q+1)⁴(q²+q+1)⁴ / (q²+1)¹⁰`. Every factor is strictly positive
/// for real `q`, so this never vanishes — the structural content behind
/// [`gram_tl_inverse`] always succeeding.
pub fn det_gram_tl_closed_form(q: f64) -> f64 {
    let q2 = q * q;
    let num = (q2 * q2 + 1.0) * (q2 - q + 1.0).powi(4) * (q2 + q + 1.0).powi(4);
    -num / (q2 + 1.0).powi(10)
}

fn det_5x5(a: &[[f64; 5]; 5]) -> f64 {
    let mut m = *a;
    let mut det = 1.0f64;
    for i in 0..5 {
        let mut best = i;
        for r in i + 1..5 {
            if m[r][i].abs() > m[best][i].abs() {
                best = r;
            }
        }
        if m[best][i].abs() < 1e-300 {
            return 0.0;
        }
        if best != i {
            m.swap(i, best);
            det = -det;
        }
        det *= m[i][i];
        let pivot = m[i][i];
        for r in i + 1..5 {
            let factor = m[r][i] / pivot;
            if factor == 0.0 {
                continue;
            }
            for j in i..5 {
                m[r][j] -= factor * m[i][j];
            }
        }
    }
    det
}

fn invert_5x5(a: &[[f64; 5]; 5]) -> Option<[[f64; 5]; 5]> {
    // Augmented matrix [A | I]; same Gauss–Jordan as `invert_6x6`.
    let mut m = [[0.0f64; 10]; 5];
    for i in 0..5 {
        for j in 0..5 {
            m[i][j] = a[i][j];
        }
        m[i][5 + i] = 1.0;
    }
    for i in 0..5 {
        let mut best = i;
        for r in i + 1..5 {
            if m[r][i].abs() > m[best][i].abs() {
                best = r;
            }
        }
        if m[best][i].abs() < 1e-15 {
            return None;
        }
        m.swap(i, best);
        let pivot = m[i][i];
        for j in 0..10 {
            m[i][j] /= pivot;
        }
        for r in 0..5 {
            if r == i {
                continue;
            }
            let factor = m[r][i];
            if factor == 0.0 {
                continue;
            }
            for j in 0..10 {
                m[r][j] -= factor * m[i][j];
            }
        }
    }
    let mut inv = [[0.0f64; 5]; 5];
    for i in 0..5 {
        for j in 0..5 {
            inv[i][j] = m[i][5 + j];
        }
    }
    Some(inv)
}

// ─── NF multiplication kernel ────────────────────────────────────────

/// Multiply an NF element by `(c · σ_gen + d · 1)`.
///
/// Mirrors `pyhecke.gram.hm` (which closes over `h = q - q^{-1}`).
/// The `gen` argument must be 0 or 1.
///
/// `nf[0..6]` is the NF basis coefficient vector `[γ, σ₀, σ₁, L₊, L₋, e⁻]`.
pub fn hm(nf: &[f64; 6], c: f64, d: f64, gen: u8, h: f64) -> [f64; 6] {
    let mut r = [0.0f64; 6];
    let tables: [(usize, &[(usize, f64)]); 6] = if gen == 0 {
        [
            (0, &[(1, c), (0, d)]),
            (1, &[(1, c * h), (0, c), (1, d)]),
            (2, &[(3, c), (2, d)]),
            (3, &[(3, c * h), (2, c), (3, d)]),
            (4, &[(5, c), (4, d)]),
            (5, &[(5, c * h), (4, c), (5, d)]),
        ]
    } else {
        [
            (0, &[(2, c), (0, d)]),
            (1, &[(4, c), (1, d)]),
            (2, &[(2, c * h), (0, c), (2, d)]),
            (3, &[(5, c), (3, d)]),
            (4, &[(4, c * h), (1, c), (4, d)]),
            (5, &[(5, c * h), (3, c), (5, d)]),
        ]
    };
    for (si, tgts) in tables.iter() {
        if nf[*si].abs() < 1e-15 {
            continue;
        }
        for (ti, co) in tgts.iter() {
            r[*ti] += nf[*si] * co;
        }
    }
    r
}

/// Markov trace of an NF vector at a given `q`.
pub fn nf_tr(nf: &[f64; 6], q: f64) -> f64 {
    let tr = trace_weights(q);
    (0..6).map(|i| nf[i] * tr[i]).sum()
}

/// Sum of NF coefficients (the net, or augmentation, of the element).
pub fn nf_net(nf: &[f64; 6]) -> f64 {
    nf.iter().sum()
}

/// Build the atom NF for (Z, N) via Hecke multiplication.
///
/// Mirrors `hecke_core.build_atom_nf` byte-for-byte. Construction:
///
/// 1. Build each nucleon via B_3 confinement + quark crossings +
///    gluon self-coupling.
/// 2. Compose in ground-state interleaved order (p, n, p, n, …).
/// 3. Apply inter-nucleon crossings between each pair:
///    pp = σ₀, nn = σ₀⁻¹, pn = ½(σ₀ + σ₀⁻¹).
/// 4. Apply pe crossings for Z electrons (σ₁⁻¹).
///
/// `h` is `hecke_h(q)` for the target q; pass `hecke_h(Q_0)` to match
/// the Python default.
pub fn build_atom_nf(z_count: u32, n_count: u32, h: f64) -> [f64; 6] {
    let a = z_count + n_count;
    if a == 0 {
        return [1.0, 0.0, 0.0, 0.0, 0.0, 0.0];
    }

    // Ground-state interleaved ordering.
    let mut ordering: Vec<u8> = Vec::with_capacity(a as usize);
    let (mut pc, mut nc) = (0u32, 0u32);
    for k in 0..a {
        if (k % 2 == 0 && pc < z_count) || nc >= n_count {
            ordering.push(b'p');
            pc += 1;
        } else {
            ordering.push(b'n');
            nc += 1;
        }
    }

    let mut nf = [1.0f64, 0.0, 0.0, 0.0, 0.0, 0.0];
    let half_h = 0.5 * h;

    for k in 0..a as usize {
        // B_3 confinement: 3x (σ₀ σ₁⁻¹)
        for _ in 0..3 {
            nf = hm(&nf, 1.0, 0.0, 0, h);
            nf = hm(&nf, 1.0, -h, 1, h);
        }

        if ordering[k] == b'p' {
            // Proton: uud
            nf = hm(&nf, 1.0, 0.0, 0, h);        // (0,1) uu → σ₀
            nf = hm(&nf, 1.0, -half_h, 0, h);    // (0,2) ud → mixed
            nf = hm(&nf, 1.0, -half_h, 1, h);    // (1,2) ud → mixed (gen 1)
        } else {
            // Neutron: udd
            nf = hm(&nf, 1.0, -half_h, 0, h);    // (0,1) ud → mixed
            nf = hm(&nf, 1.0, -half_h, 0, h);    // (0,2) ud → mixed
            nf = hm(&nf, 1.0, -h, 1, h);         // (1,2) dd → σ₁⁻¹
        }

        // Gluon self-coupling: 2 × σ₀
        nf = hm(&nf, 1.0, 0.0, 0, h);
        nf = hm(&nf, 1.0, 0.0, 0, h);

        // Inter-nucleon crossings with all previous nucleons
        for prev in 0..k {
            let (ti, tj) = (ordering[prev], ordering[k]);
            if ti == b'p' && tj == b'p' {
                nf = hm(&nf, 1.0, 0.0, 0, h);         // pp: σ₀
            } else if ti == b'n' && tj == b'n' {
                nf = hm(&nf, 1.0, -h, 0, h);          // nn: σ₀⁻¹
            } else {
                // pn/np interface. This reproduces the `-half_h` that used
                // to be inlined here, bit-identically — the point of naming
                // the convention is that `GRAM_PN_CONVENTION` is NOT the
                // canonical one: bring_color_weighted differs by h*delta/4.
                // `build_atom_nf` carries only `h`, hence the h-only entry
                // point, which needs no inversion for this convention.
                let d_pn = crate::color_weight::pn_offset_from_h(
                    h,
                    crate::color_weight::GRAM_PN_CONVENTION,
                );
                nf = hm(&nf, 1.0, d_pn, 0, h);
            }
        }
    }

    // Electrons: pe crossing (EM channel, gen=1)
    for _ in 0..z_count {
        nf = hm(&nf, 1.0, -h, 1, h);
    }

    nf
}

// ─── Per-generator Wedderburn volumes ────────────────────────────────

/// Per-generator Wedderburn-channel state: (a, b) for the standard
/// 2-dim irrep, sp for symmetric (1-dim), ap for alternating (1-dim).
#[derive(Debug, Clone, Copy)]
struct ChannelState {
    a: f64,
    b: f64,
    sp: f64,
    ap: f64,
}

impl ChannelState {
    fn new() -> Self {
        Self { a: 0.0, b: 1.0, sp: 1.0, ap: 1.0 }
    }

    fn apply(&mut self, c: f64, d: f64, h: f64, q: f64, qi: f64) {
        let a_new = self.a * c * h + self.a * d + self.b * c;
        let b_new = self.a * c + self.b * d;
        self.a = a_new;
        self.b = b_new;
        self.sp *= c * q + d;
        self.ap *= -c * qi + d;
    }
}

/// Volume entry: `(sym, std, alt, full)` for one generator.
#[derive(Debug, Clone, Copy)]
pub struct VolumeEntry {
    pub sym: f64,
    pub std: f64,
    pub alt: f64,
    pub full: f64,
}

fn _proton_g0(h: f64) -> [(f64, f64); 6] {
    // B_3: 3x (1, 0), then uu=(1,0), ud=(1,-h/2), gluon=(1,0), (1,0)
    [
        (1.0, 0.0),
        (1.0, 0.0),
        (1.0, 0.0),
        (1.0, 0.0),
        (1.0, -0.5 * h),
        (1.0, 0.0),
    ]
}

fn _proton_g0_full(h: f64) -> Vec<(f64, f64)> {
    vec![
        (1.0, 0.0), (1.0, 0.0), (1.0, 0.0),  // B_3
        (1.0, 0.0),                           // uu
        (1.0, -0.5 * h),                      // ud
        (1.0, 0.0), (1.0, 0.0),               // 2 gluons
    ]
}

fn _proton_g1(h: f64) -> Vec<(f64, f64)> {
    vec![
        (1.0, -h), (1.0, -h), (1.0, -h),      // B_3
        (1.0, -0.5 * h),                       // ud (gen 1)
    ]
}

fn _neutron_g0(h: f64) -> Vec<(f64, f64)> {
    vec![
        (1.0, 0.0), (1.0, 0.0), (1.0, 0.0),  // B_3
        (1.0, -0.5 * h),                      // ud
        (1.0, -0.5 * h),                      // ud
        (1.0, 0.0), (1.0, 0.0),               // 2 gluons
    ]
}

fn _neutron_g1(h: f64) -> Vec<(f64, f64)> {
    vec![
        (1.0, -h), (1.0, -h), (1.0, -h),      // B_3
        (1.0, -h),                             // dd (gen 1)
    ]
}

/// Per-generator Wedderburn volumes V̂_i^full for the atom braid.
///
/// Mirrors `hecke_core.atom_per_generator_volumes`. Returns one
/// `VolumeEntry` per generator (length `n_gens_total`):
///   * `include_inter=true`: `n_gens_total = 3A - 1` (the physical
///     atom braid with pp/nn/pn inter-nucleon crossings)
///   * `include_inter=false`: `n_gens_total = 2A` (free disconnected
///     baseline)
///
/// `crossings_per_pair` (or explicit `m_pp`, `m_pn`, `m_nn`) controls
/// inter-nucleon crossing multiplicity. Pass `None` for the defaults.
pub fn atom_per_generator_volumes(
    z_count: u32,
    n_count: u32,
    include_inter: bool,
    crossings_per_pair: u32,
    m_pp: Option<u32>,
    m_pn: Option<u32>,
    m_nn: Option<u32>,
    q: f64,
) -> Vec<VolumeEntry> {
    let a = z_count + n_count;
    if a == 0 {
        return vec![];
    }

    let qi = 1.0 / q;
    let h = q - qi;

    let ordering: Vec<u8> = {
        let mut v = Vec::with_capacity(a as usize);
        for _ in 0..z_count { v.push(b'p'); }
        for _ in 0..n_count { v.push(b'n'); }
        v
    };

    let n_gens_total: usize = if include_inter {
        (3 * a - 1) as usize
    } else {
        (2 * a) as usize
    };
    let mut states: Vec<ChannelState> = vec![ChannelState::new(); n_gens_total];

    for k in 0..a as usize {
        let nuc = ordering[k];
        let (intra0, intra1) = if nuc == b'p' {
            (_proton_g0_full(h), _proton_g1(h))
        } else {
            (_neutron_g0(h), _neutron_g1(h))
        };
        let (base_g0, base_g1) = if include_inter {
            (3 * k, 3 * k + 1)
        } else {
            (2 * k, 2 * k + 1)
        };
        for &(c, d) in &intra0 {
            states[base_g0].apply(c, d, h, q, qi);
        }
        for &(c, d) in &intra1 {
            states[base_g1].apply(c, d, h, q, qi);
        }
        if include_inter && (k as u32) < a - 1 {
            let i = 3 * k + 2;
            let next_nuc = ordering[k + 1];
            let (c, d, m) = if nuc == b'p' && next_nuc == b'p' {
                (1.0f64, 0.0f64, m_pp.unwrap_or(crossings_per_pair))
            } else if nuc == b'n' && next_nuc == b'n' {
                (1.0, -h, m_nn.unwrap_or(crossings_per_pair))
            } else {
                // pn/np interface — see the note in `build_atom_nf`; same
                // convention, same bit-identical value, `q` in scope here.
                let d_pn = crate::color_weight::pn_offset(
                    q,
                    crate::color_weight::GRAM_PN_CONVENTION,
                );
                (1.0, d_pn, m_pn.unwrap_or(crossings_per_pair))
            };
            for _ in 0..m {
                states[i].apply(c, d, h, q, qi);
            }
        }
    }

    // Convention D (owner ruling 2026-11-18, PR #8521): the per-generator
    // volume is the Markov trace of the generator's word a*sigma_i + b,
    // i.e. z*a + b with z = q^3/(q^2+1). It is the same in every H_n by the
    // Markov property. The q-Plancherel block mixture
    // W_SYM*sym + W_STD*(z*a+b) + W_ALT*alt that stood here is retired;
    // `sym` and `alt` are still reported per block.
    let z_mark = markov_z(q);
    let mut out = Vec::with_capacity(n_gens_total);
    for s in states.iter() {
        let v_std = z_mark * s.a + s.b;
        out.push(VolumeEntry {
            sym: s.sp,
            std: v_std,
            alt: s.ap,
            full: v_std,
        });
    }
    out
}

// ─── Serialization ───────────────────────────────────────────────────

/// JSON-serializable record of a Gram-matrix computation.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct GramCertificate {
    pub q: f64,
    pub z: f64,
    pub h: f64,
    pub n: u32,
    pub basis: Vec<String>,
    pub trace_weights: Vec<f64>,
    pub matrix: Vec<Vec<f64>>,
    /// Inverse on the quotient `H_3(q)/rad`, NOT a 6x6 inverse.
    ///
    /// RENAMED from `inverse` (2026-08-15). Under convention D with the
    /// correct trace the form is singular, so the old field named an object
    /// that does not exist. Renaming rather than refilling it is deliberate:
    /// a consumer keyed on `inverse` now fails loudly instead of silently
    /// receiving a different matrix — they differ exactly on the radical.
    pub quotient_inverse: Vec<Vec<f64>>,
    /// The null direction (q-antisymmetriser), in closed form.
    pub radical: Vec<f64>,
    /// Determinant of `matrix`. Zero up to f64 noise under convention D;
    /// see `gram_radical` for the exact statement.
    pub determinant: f64,
}

pub fn certificate_at(q: f64) -> GramCertificate {
    let g = gram_matrix(q);
    let qinv = gram_quotient_inverse(q);
    GramCertificate {
        q,
        z: markov_z(q),
        h: hecke_h(q),
        n: 3,
        basis: NF_NAMES.iter().map(|s| s.to_string()).collect(),
        // Convention D (qou-m7py): report the production Markov trace
        // (`h·z² + z`), matching `matrix`/`quotient_inverse`/`radical` below.
        // The legacy `z³` weights live in `trace_weights` for reference only.
        trace_weights: trace_weights_markov(q).to_vec(),
        matrix: g.iter().map(|r| r.to_vec()).collect(),
        quotient_inverse: qinv.iter().map(|r| r.to_vec()).collect(),
        radical: gram_radical(q).to_vec(),
        determinant: det_6x6(&g),
    }
}

pub fn det_6x6(a: &[[f64; 6]; 6]) -> f64 {
    let mut m = *a;
    let mut det = 1.0f64;
    for i in 0..6 {
        let mut best = i;
        for r in i + 1..6 {
            if m[r][i].abs() > m[best][i].abs() {
                best = r;
            }
        }
        if m[best][i].abs() < 1e-15 {
            return 0.0;
        }
        if best != i {
            m.swap(i, best);
            det = -det;
        }
        det *= m[i][i];
        let pivot = m[i][i];
        for j in i..6 {
            m[i][j] /= pivot;
        }
        for r in i + 1..6 {
            let factor = m[r][i];
            if factor == 0.0 {
                continue;
            }
            for j in i..6 {
                m[r][j] -= factor * m[i][j];
            }
        }
    }
    det
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn z_at_q0_matches_python() {
        // Pin history:
        //   0.4993203340335982  convention C, muon pin (pre-2026-08-09)
        //   0.6126880505455892  convention D, muon pin
        //   0.6126880371464652  convention D, PROTON pin (2026-08-15 re-pin)
        //
        // The name of this test is finally accurate: as of the re-pin the
        // value is BIT-IDENTICAL to `pyhecke.gram.z`, not merely close. The
        // tolerance is kept rather than switched to `==` so the test reports
        // a drift instead of a bare inequality, but the two sides now agree
        // exactly at the proton pin.
        let z = markov_z(Q_0);
        assert!((z - 0.6126880371464652).abs() < 1e-14, "z = {}", z);
        // Guard the re-pin directly: this is NOT the muon-pin value.
        assert!((z - 0.6126880505455892).abs() > 1e-9, "still on the muon pin");
    }

    #[test]
    fn h_at_q0() {
        let h = hecke_h(Q_0);
        // q - 1/q at q_0
        let expected = Q_0 - 1.0 / Q_0;
        assert!((h - expected).abs() < 1e-15);
    }

    #[test]
    fn gram_diagonal_g00_is_one() {
        let g = gram_matrix(Q_0);
        assert!((g[0][0] - 1.0).abs() < 1e-14);
    }

    /// The 6x6 inverse is GONE, and the quotient inverse replaces it.
    ///
    /// Was `gram_inverse_is_right_inverse`, asserting `G * G^-1 = I`. Under
    /// convention D with the correct trace that identity is FALSE — the form
    /// is singular — so the test was reporting the mathematics correctly and
    /// is replaced rather than relaxed. `G^-1` is not "harder to compute"
    /// here; it does not exist.
    #[test]
    fn quotient_inverse_replaces_the_absent_6x6_inverse() {
        let g = gram_matrix(Q_0);
        let p = gram_quotient_inverse(Q_0);

        // Singular: no 6x6 inverse to be a right-inverse OF.
        assert!(det_6x6(&g).abs() < 1e-12, "det = {}", det_6x6(&g));

        let mul = |a: &[[f64; 6]; 6], b: &[[f64; 6]; 6]| {
            let mut o = [[0.0f64; 6]; 6];
            for i in 0..6 {
                for j in 0..6 {
                    o[i][j] = (0..6).map(|k| a[i][k] * b[k][j]).sum();
                }
            }
            o
        };
        // Moore-Penrose in place of the inverse identity.
        let gpg = mul(&mul(&g, &p), &g);
        for i in 0..6 {
            for j in 0..6 {
                assert!((gpg[i][j] - g[i][j]).abs() < 1e-8, "G P G != G at {i},{j}");
            }
        }
        // G*P is NOT the identity, and asserting so guards against anyone
        // "fixing" this back into the old test.
        let gp = mul(&g, &p);
        let off = (0..6).map(|i| (gp[i][i] - 1.0).abs()).fold(0.0, f64::max);
        assert!(off > 1e-6, "G*P should NOT be I under convention D");
    }

    /// Gram determinant at `Q_0` — ZERO, which is the whole point.
    ///
    /// Pin history, each step a real change rather than a re-tune:
    ///   -0.3608011166161873   convention C, muon pin, z^3 trace
    ///   -0.15201823561588593  convention D, muon pin, z^3 trace
    ///   -0.15201823908521292  convention D, PROTON pin, z^3 trace
    ///    0                    convention D, proton pin, CORRECT trace
    ///
    /// The last step is the 2026-08-15 TR_M[5] flip. Asserting a tolerance
    /// rather than `== 0.0` on principle — this f64 path happens to return
    /// literal zero here, but that is luck of the arithmetic, not a
    /// guarantee, and the EXACT statement (det = 0 over Q, rank 5) lives in
    /// the Python side's `test_gram_determinant_is_exactly_zero_over_Q`,
    /// which can prove it because convention D makes the Gram rational. No
    /// f64 determinant can distinguish singular from very small.
    #[test]
    fn det_at_q0_is_zero_under_the_correct_trace() {
        let d = det_6x6(&gram_matrix(Q_0));
        assert!(d.abs() < 1e-12, "det = {d}");
    }

    #[test]
    fn gram_first_row_matches_trace_weights() {
        // G[0, j] = tr_M(1 · b_j) = tr_M(b_j) = TR_M[j]
        let g = gram_matrix(Q_0);
        let tr = trace_weights(Q_0);
        for j in 0..6 {
            assert!(
                (g[0][j] - tr[j]).abs() < 1e-14,
                "G[0][{}] = {} vs TR_M[{}] = {}",
                j, g[0][j], j, tr[j]
            );
        }
    }

    #[test]
    fn hm_identity_on_gamma() {
        // hm(γ, 1, 0, 0) should give σ_0 (basis index 1)
        let nf = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0];
        let out = hm(&nf, 1.0, 0.0, 0, hecke_h(Q_0));
        assert!((out[1] - 1.0).abs() < 1e-12);
        for i in [0, 2, 3, 4, 5] {
            assert!(out[i].abs() < 1e-12);
        }
    }

    #[test]
    fn nf_tr_of_gamma_is_one() {
        let nf = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0];
        assert!((nf_tr(&nf, Q_0) - 1.0).abs() < 1e-14);
    }

    #[test]
    fn nf_net_sum() {
        let nf = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0];
        assert!((nf_net(&nf) - 21.0).abs() < 1e-14);
    }

    #[test]
    fn build_atom_nf_hydrogen() {
        // H (Z=1, N=0): one nucleon (proton) + one electron
        let h = hecke_h(Q_0);
        let nf = build_atom_nf(1, 0, h);
        // Must be a finite length-6 result
        assert!(nf.iter().all(|x| x.is_finite()));
        // Non-trivial: at least one coordinate should be non-zero
        assert!(nf.iter().any(|x| x.abs() > 1e-10));
    }

    #[test]
    fn build_atom_nf_vacuum() {
        // (0, 0) → identity NF
        let h = hecke_h(Q_0);
        let nf = build_atom_nf(0, 0, h);
        assert!((nf[0] - 1.0).abs() < 1e-14);
        for i in 1..6 {
            assert!(nf[i].abs() < 1e-14);
        }
    }

    // ─── Convention-D Markov repair: correct trace, radical, quotient ───
    // These exercise `trace_weights_markov` / `gram_matrix_markov` /
    // `gram_radical` / `gram_quotient_inverse`, which are ADDITIVE — nothing
    // in the shipped pipeline calls them yet. They exist so the correct
    // objects are verified before the gated switch, not after.

    /// `TR_M[5]` is `h·z² + z`, derived — not read off the implementation.
    ///
    /// Was `markov_trace_differs_only_at_e_minus`, which compared
    /// `trace_weights` against `trace_weights_markov`. The 2026-08-15 flip
    /// made those the same function, so that comparison is now vacuous and
    /// is replaced by asserting the VALUE against its definition, plus a
    /// guard that it is not the old `z³`.
    #[test]
    fn trace_weights_carries_the_correct_markov_value() {
        let tr = trace_weights(Q_0);
        let z = markov_z(Q_0);
        let h = hecke_h(Q_0);
        assert!((tr[0] - 1.0).abs() < 1e-15);
        assert!((tr[1] - z).abs() < 1e-15);
        assert!((tr[3] - z * z).abs() < 1e-15);
        assert!((tr[5] - (h * z * z + z)).abs() < 1e-15);
        // Guard the flip: NOT the pre-2026-05-19 z^3, which differs by >200%.
        assert!((tr[5] - z * z * z).abs() > 1e-3,
                "TR_M[5] regressed to z^3: {}", tr[5]);
        // The alias must track it, or a caller of either gets a different Gram.
        assert_eq!(trace_weights_markov(Q_0), tr);
    }

    /// The Gram is singular — the direct consequence of the correct trace.
    ///
    /// Was `markov_gram_is_singular_and_legacy_is_not`; there is no "legacy"
    /// any more, so the contrast is asserted against the z^3 weight built
    /// inline rather than against a second live function.
    #[test]
    fn gram_is_singular_under_the_correct_trace() {
        assert!(det_6x6(&gram_matrix(Q_0)).abs() < 1e-12);
        assert_eq!(gram_matrix_markov(Q_0), gram_matrix(Q_0));

        // With the OLD z^3 weight it would not be — this is what made the
        // bug survivable, and why the fix could not be applied in isolation.
        let z = markov_z(Q_0);
        let legacy = [1.0, z, z, z * z, z * z, z * z * z];
        let gl = gram_from_weights(Q_0, &legacy);
        assert!(det_6x6(&gl).abs() > 1e-3,
                "the z^3 Gram should be NON-singular: {}", det_6x6(&gl));
    }

    /// The closed-form q-antisymmetriser annihilates the Gram.
    #[test]
    fn radical_annihilates_the_gram() {
        let v = gram_radical(Q_0);
        assert!((v[0] - 1.0).abs() < 1e-15);
        assert!((v[1] - (-1.0 / Q_0)).abs() < 1e-15);
        assert!((v[5] - (-1.0 / Q_0).powi(3)).abs() < 1e-15);

        let g = gram_matrix(Q_0);
        let worst = (0..6)
            .map(|i| (0..6).map(|j| g[i][j] * v[j]).sum::<f64>().abs())
            .fold(0.0, f64::max);
        assert!(worst < 1e-12, "G @ radical = {worst}");

        // Not a null vector of the z^3 form — the radical exists BECAUSE the
        // trace is right.
        let z = markov_z(Q_0);
        let gl = gram_from_weights(Q_0, &[1.0, z, z, z * z, z * z, z * z * z]);
        let wl = (0..6)
            .map(|i| (0..6).map(|j| gl[i][j] * v[j]).sum::<f64>().abs())
            .fold(0.0, f64::max);
        assert!(wl > 1e-3, "z^3 Gram should NOT be annihilated: {wl}");
    }

    /// Moore-Penrose defining identities, plus the property that actually
    /// distinguishes a quotient inverse from a regularised fake: it must
    /// ANNIHILATE the radical.
    #[test]
    fn quotient_inverse_is_the_pseudoinverse() {
        let g = gram_matrix_markov(Q_0);
        let p = gram_quotient_inverse(Q_0);

        let mul = |a: &[[f64; 6]; 6], b: &[[f64; 6]; 6]| {
            let mut o = [[0.0f64; 6]; 6];
            for i in 0..6 {
                for j in 0..6 {
                    o[i][j] = (0..6).map(|k| a[i][k] * b[k][j]).sum();
                }
            }
            o
        };

        let gpg = mul(&mul(&g, &p), &g);
        let pgp = mul(&mul(&p, &g), &p);
        for i in 0..6 {
            for j in 0..6 {
                assert!((gpg[i][j] - g[i][j]).abs() < 1e-8, "G P G != G at {},{}", i, j);
                assert!((pgp[i][j] - p[i][j]).abs() < 1e-8, "P G P != P at {},{}", i, j);
            }
        }

        let v = gram_radical(Q_0);
        let max: f64 = (0..6)
            .map(|i| (0..6).map(|j| p[i][j] * v[j]).sum::<f64>().abs())
            .fold(0.0, f64::max);
        assert!(max < 1e-8, "G_PINV must kill the radical, got {}", max);
    }

    /// Cross-check against `numpy.linalg.pinv` via `pyhecke.gram.G_PINV`.
    ///
    /// Values captured at the PROTON pin, which is what pyhecke reads --
    /// deliberately NOT `Q_0` (this crate's constant is still the muon pin;
    /// re-pinning it is a separate owner decision, see the module note). So
    /// this test passes the proton value explicitly and is unaffected by, and
    /// does not prejudge, that decision.
    #[test]
    fn quotient_inverse_matches_python_pinv() {
        const Q_PROTON: f64 = 1.1099785827513808;
        let p = gram_quotient_inverse(Q_PROTON);
        // pyhecke.gram.G_PINV row 0 at the proton pin.
        let expected_row0 = [
            0.9012212173018036,
            0.12260020756551251,
            0.1226002075655125,
            -0.40169476804296567,
            -0.40169476804296567,
            0.03862177933380513,
        ];
        for j in 0..6 {
            assert!(
                (p[0][j] - expected_row0[j]).abs() < 1e-9,
                "P[0][{}] = {} vs numpy {}", j, p[0][j], expected_row0[j]
            );
        }
        // Symmetry, which pinv of a symmetric matrix must have.
        for i in 0..6 {
            for j in 0..6 {
                assert!((p[i][j] - p[j][i]).abs() < 1e-10, "asymmetric at {},{}", i, j);
            }
        }
    }

    // ─── Temperley–Lieb quotient (qou-cds2 / qou-8iru) ───────────────

    /// The five TL entries are the full form's, on the 321-avoiding words.
    ///
    /// Pinned against `pyhecke.tl.tl_gram_mp(3, 60)` at the proton-pinned
    /// `q₀`, printed at 17 significant digits. This is the check that the
    /// basis-order difference between the two implementations really is
    /// immaterial at `n = 3`, rather than an assumption.
    #[test]
    fn tl_gram_matches_python_at_q0() {
        const PY: [[f64; 5]; 5] = [
            [
                1.0,
                0.61268803714646525,
                0.61268803714646525,
                0.37538663086238838,
                0.37538663086238838,
            ],
            [
                0.61268803714646525,
                1.1280887441143538,
                0.37538663086238838,
                0.69116647835844453,
                0.69116647835844453,
            ],
            [
                0.61268803714646525,
                0.37538663086238838,
                1.1280887441143538,
                0.69116647835844453,
                0.69116647835844453,
            ],
            [
                0.37538663086238838,
                0.69116647835844453,
                0.69116647835844453,
                0.51988210134553457,
                1.2725842145975,
            ],
            [
                0.37538663086238838,
                0.69116647835844453,
                0.69116647835844453,
                1.2725842145975,
                0.51988210134553457,
            ],
        ];
        let g = gram_matrix_tl(Q_0);
        for i in 0..5 {
            for j in 0..5 {
                assert!(
                    (g[i][j] - PY[i][j]).abs() < 1e-12,
                    "entry ({i},{j}): rust {} vs python {}",
                    g[i][j],
                    PY[i][j]
                );
            }
        }
    }

    /// The TL form has a genuine inverse where the full form has none.
    #[test]
    fn tl_gram_inverse_is_a_real_inverse() {
        let g = gram_matrix_tl(Q_0);
        let inv = gram_tl_inverse(Q_0).expect("TL form is non-singular for real q > 0");
        for i in 0..5 {
            for j in 0..5 {
                let entry: f64 = (0..5).map(|k| g[i][k] * inv[k][j]).sum();
                let want = if i == j { 1.0 } else { 0.0 };
                assert!(
                    (entry - want).abs() < 1e-10,
                    "G·G⁻¹ ({i},{j}) = {entry}, want {want}"
                );
            }
        }
    }

    /// The LU determinant agrees with PR #5572's closed form.
    ///
    /// Two independent routes to the same number: Gaussian elimination on the
    /// assembled matrix, versus the factored rational expression. Checked
    /// across a range of `q`, not only at the substrate anchor, since the
    /// closed form is what licenses the "every real q > 0" claim.
    #[test]
    fn tl_determinant_matches_the_closed_form() {
        for &q in &[1.01f64, 1.05, Q_0, 1.5, 2.0, 3.0] {
            let lu = det_gram_tl(q);
            let cf = det_gram_tl_closed_form(q);
            let scale = cf.abs().max(1e-12);
            assert!(
                (lu - cf).abs() / scale < 1e-9,
                "q={q}: LU {lu} vs closed form {cf}"
            );
        }
    }

    /// The closed form never vanishes — the structural content of the repair.
    ///
    /// Every factor is strictly positive for real `q`, so the determinant is
    /// strictly negative and the inverse always exists. Contrast
    /// `gram_is_singular_under_the_correct_trace` on the full form.
    #[test]
    fn tl_determinant_never_vanishes_for_real_q() {
        for &q in &[0.1f64, 0.5, 1.0, Q_0, 2.0, 10.0, 100.0] {
            let d = det_gram_tl_closed_form(q);
            assert!(d < 0.0, "q={q}: det {d} is not strictly negative");
            assert!(gram_tl_inverse(q).is_some(), "q={q}: inverse should exist");
        }
    }

    /// The excluded word is the one the full form's radical needs.
    ///
    /// `gram_radical` has a nonzero `e⁻` component, so dropping index 5 is
    /// what removes the null direction — this is *why* the five survive,
    /// rather than a lucky choice of five.
    #[test]
    fn dropping_e_minus_is_what_kills_the_radical() {
        let r = gram_radical(Q_0);
        assert!(
            r[5].abs() > 1e-6,
            "radical must load the dropped basis element, got {}",
            r[5]
        );
        assert!(!TL_BASIS_INDICES.contains(&5));
    }
}
