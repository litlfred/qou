//! PyO3 native acceleration layer for `pyhecke`.
//!
//! Re-exposes the hottest hecke-engine kernels as a Python extension
//! module `pyhecke_native`. No NumPy dependency — returns nested
//! Python lists that `pyhecke.bridge` converts on demand. This keeps
//! the wheel small and the build simple.

use hecke_engine::{
    geck_pfeiffer, gram, laurent_hecke_element, littlewood_richardson, reduce_laurent, seminormal,
    seminormal_mn, seminormal_mpfr, tr_m_word_lq as rust_tr_m_word_lq, wenzl_lr,
};
use pyo3::prelude::*;

/// Markov parameter z = 1 / (q^{1/2} + q^{-1/2}).
#[pyfunction]
fn markov_z(q: f64) -> f64 {
    gram::markov_z(q)
}

/// Hecke relation coefficient h = q - q^{-1}.
#[pyfunction]
fn hecke_h(q: f64) -> f64 {
    gram::hecke_h(q)
}

/// Markov-trace weights on the NF basis as a length-6 list.
#[pyfunction]
fn trace_weights(q: f64) -> Vec<f64> {
    gram::trace_weights(q).to_vec()
}

/// Gram matrix G_ij = tr_M(b_i · b_j) as a 6x6 list of lists.
#[pyfunction]
fn gram_matrix(q: f64) -> Vec<Vec<f64>> {
    gram::gram_matrix(q).iter().map(|r| r.to_vec()).collect()
}

/// Gram determinant — delegates to shared `hecke_engine::gram::det_6x6`.
#[pyfunction]
fn gram_determinant(q: f64) -> f64 {
    gram::det_6x6(&gram::gram_matrix(q))
}

/// Gram inverse as a 6x6 list of lists.
#[pyfunction]
fn gram_inverse(q: f64) -> Vec<Vec<f64>> {
    gram::gram_inverse(q).iter().map(|r| r.to_vec()).collect()
}

/// NF multiplication: multiply NF vector by `(c · σ_gen + d · 1)`.
///
/// Takes the 6-element NF vector and optional `h` (defaults to
/// `hecke_h(q_0)` = q_0 - q_0^{-1}). Returns a new 6-element list.
#[pyfunction]
#[pyo3(signature = (nf, c, d, gen, h=None))]
fn hm(nf: Vec<f64>, c: f64, d: f64, gen: u8, h: Option<f64>) -> PyResult<Vec<f64>> {
    if nf.len() != 6 {
        return Err(pyo3::exceptions::PyValueError::new_err(
            format!("nf must have exactly 6 elements, got {}", nf.len()),
        ));
    }
    let arr: [f64; 6] = [nf[0], nf[1], nf[2], nf[3], nf[4], nf[5]];
    let h_val = h.unwrap_or_else(|| gram::hecke_h(gram::Q_0));
    Ok(gram::hm(&arr, c, d, gen, h_val).to_vec())
}

/// Markov trace of a 6-element NF vector at a given `q`.
#[pyfunction]
#[pyo3(signature = (nf, q=None))]
fn nf_tr(nf: Vec<f64>, q: Option<f64>) -> PyResult<f64> {
    if nf.len() != 6 {
        return Err(pyo3::exceptions::PyValueError::new_err(
            format!("nf must have exactly 6 elements, got {}", nf.len()),
        ));
    }
    let arr: [f64; 6] = [nf[0], nf[1], nf[2], nf[3], nf[4], nf[5]];
    Ok(gram::nf_tr(&arr, q.unwrap_or(gram::Q_0)))
}

/// Sum of NF coefficients.
#[pyfunction]
fn nf_net(nf: Vec<f64>) -> PyResult<f64> {
    Ok(nf.iter().sum())
}

/// Build the full atom NF for (Z, N) via Hecke multiplication.
///
/// Mirrors `hecke_core.build_atom_nf`: proton / neutron B_3 confinement
/// + quark crossings + gluon self-coupling + inter-nucleon crossings +
/// electron (σ₁⁻¹) insertion. Returns a length-6 list of f64.
///
/// `h` defaults to `hecke_h(Q_0) = Q_0 - Q_0^{-1}` (the physical
/// substrate value). Pass an explicit `h` for alternative q.
#[pyfunction]
#[pyo3(signature = (z, n, h=None))]
fn build_atom_nf(z: u32, n: u32, h: Option<f64>) -> Vec<f64> {
    let h_val = h.unwrap_or_else(|| gram::hecke_h(gram::Q_0));
    gram::build_atom_nf(z, n, h_val).to_vec()
}

/// Per-generator Wedderburn volumes for the atom braid.
///
/// Returns a list of dicts `{sym, std, alt, full}` matching
/// `hecke_core.atom_per_generator_volumes`. `n_gens_total` =
/// `3A - 1` when `include_inter=True` (physical atom) else `2A`
/// (free baseline).
#[pyfunction]
#[pyo3(signature = (
    z, n,
    include_inter=true,
    crossings_per_pair=1,
    m_pp=None, m_pn=None, m_nn=None,
    q=None,
))]
#[allow(clippy::too_many_arguments)]
fn atom_per_generator_volumes(
    py: Python<'_>,
    z: u32,
    n: u32,
    include_inter: bool,
    crossings_per_pair: u32,
    m_pp: Option<u32>,
    m_pn: Option<u32>,
    m_nn: Option<u32>,
    q: Option<f64>,
) -> PyResult<PyObject> {
    let q_val = q.unwrap_or(gram::Q_0);
    let vols = gram::atom_per_generator_volumes(
        z, n, include_inter, crossings_per_pair,
        m_pp, m_pn, m_nn, q_val,
    );
    let list = pyo3::types::PyList::empty(py);
    for v in vols {
        let d = pyo3::types::PyDict::new(py);
        d.set_item("sym", v.sym)?;
        d.set_item("std", v.std)?;
        d.set_item("alt", v.alt)?;
        d.set_item("full", v.full)?;
        list.append(d)?;
    }
    Ok(list.into())
}

/// Hoefsmit seminormal character `χ_λ(β)` of a braid `β` for partition
/// `shape` at parameter `q`.
///
/// `shape`: partition λ ⊢ n as a list of descending part sizes.
/// `word`: braid as `[(sign, generator_index_1based), ...]`,
///   `sign ∈ {+1, -1}`, `generator_index ∈ {1, ..., n-1}`.
/// `q`: Hecke parameter (substrate value).
///
/// Returns `χ_λ(β) ∈ ℝ`.  Uses the sparse Hoefsmit kernel; gives a
/// ~50–100× speedup over the pure-Python implementation for `n ≥ 9`.
#[pyfunction]
fn chi_lambda_braid(shape: Vec<usize>, word: Vec<(i32, u32)>, q: f64) -> f64 {
    seminormal::chi_lambda_braid(&shape, &word, q)
}

/// **F3.2.ζ — q-character on a sequence of Hecke factors `c·σ + d·I`.**
///
/// `chi_q_atomic(shape, factors, q)` returns
/// `χ_λ(Π_i (c_i · σ_{g_i} + d_i · I))` for partition `λ ⊢ n` at
/// substrate parameter `q`.
///
/// `factors`: list of `(c, d, gen_1based)` triples, applied
/// **left-to-right** (factor at position 0 is rightmost in the
/// matrix product).
///
/// Use case: QOU atomic-braid Hecke characters with proton/neutron
/// `(c, d)` per crossing — what `chi_lambda_braid` (which only
/// takes `(sign, gen)` braid words) cannot handle. Unlocks A=12+
/// q-Hecke per-braid evaluation (P2.2c-12C).
///
/// Per-basis-vector iterative trace; O(dim²·k) per partition;
/// ≪ 1 s in release-optimised Rust for typical atomic braids.
#[pyfunction]
fn chi_q_atomic(shape: Vec<usize>, factors: Vec<(f64, f64, u32)>, q: f64) -> f64 {
    seminormal::chi_q_atomic(&shape, &factors, q)
}

/// Enumerate all partitions of `n` as a list of lists.
#[pyfunction]
fn partitions_of(n: usize) -> Vec<Vec<usize>> {
    seminormal::partitions_of(n)
}

/// **Classical Murnaghan-Nakayama character** `χ^λ(μ)`.
///
/// Computes the irreducible character of the symmetric group `S_n`
/// at the conjugacy class of cycle type `μ`, on the irrep indexed by
/// partition `λ`.  Returns an integer (classical MN values are in ℤ).
///
/// **Cost**: O(n² · #(border-strip-tableaux)) per character.  For
/// cross-validation with the Hoefsmit seminormal kernel at q = 1.
///
/// `lambda`: partition of n.
/// `mu`: cycle type (list of cycle lengths in any order).
#[pyfunction]
fn mn_chi(lambda: Vec<usize>, mu: Vec<usize>) -> i64 {
    seminormal_mn::mn_chi(&lambda, &mu)
}

/// **Debug helper**: returns the reduced Hecke-basis expansion as a list
/// of `(perm_one_line, length, cycle_type, coeff_terms)` for each
/// basis element after `reduce_basis_to_minimal_length`.
#[pyfunction]
fn debug_reduced_basis(n: usize, word: Vec<(i32, u32)>) -> Vec<(Vec<usize>, usize, Vec<usize>, Vec<(i32, String)>)> {
    let initial = geck_pfeiffer::braid_to_hecke(n, &word);
    let reduced = geck_pfeiffer::reduce_basis_to_minimal_length(&initial);
    let mut out = Vec::new();
    for (w, c) in reduced {
        let one_line = w.0.clone();
        let len = w.length();
        // cycle type
        let n = w.n();
        let mut visited = vec![false; n];
        let mut cycles = Vec::new();
        for start in 0..n {
            if visited[start] { continue; }
            let mut clen = 0;
            let mut j = start;
            while !visited[j] {
                visited[j] = true;
                j = w.0[j];
                clen += 1;
            }
            cycles.push(clen);
        }
        cycles.sort_by(|a, b| b.cmp(a));
        let coeff_terms: Vec<(i32, String)> = c.terms.into_iter()
            .map(|(he, bi)| (he, bi.to_string()))
            .collect();
        out.push((one_line, len, cycles, coeff_terms));
    }
    out
}

/// **F3.2.η — correct chi via basis expansion + Hoefsmit per T_w.**
///
/// Computes `χ_λ(T_β; q)` correctly at any q by:
///   1. Expanding T_β = Σ c_w · T_w in the Hecke basis.
///   2. For each basis element, finding a reduced word for w and
///      evaluating Hoefsmit on it.
///   3. Summing c_w · χ_λ(T_w) with c_w evaluated as f64 at q.
///
/// Returns f64 character value.  No MN speedup vs direct Hoefsmit
/// but validates the basis-expansion infrastructure.
#[pyfunction]
fn chi_via_gp_hoefsmit(
    lambda: Vec<usize>,
    n: usize,
    word: Vec<(i32, u32)>,
    q: f64,
) -> f64 {
    geck_pfeiffer::chi_lambda_via_gp_hoefsmit(&lambda, n, &word, q)
}

/// **F3.2.γ — q-character via Geck-Pfeiffer Hecke-basis expansion** *(EXPERIMENTAL).*
///
/// Computes `χ_λ(T_β; q)` for an arbitrary braid word `β` by:
///   1. Expanding `T_β = Σ c_w(q) · T_w` in the canonical Hecke basis.
///   2. Computing `χ_λ(T_w; q)` via q-MN on cycle type of w (a class
///      function on canonical T_w).
///   3. Summing `Σ c_w(q) · χ_λ(T_w; q)`.
///
/// Returns the q-Laurent polynomial as `[(half_exp, coeff_str), ...]`.
///
/// **WARNING (Copilot review #r3144...): structurally incomplete at q ≠ 1.**
/// The underlying [`geck_pfeiffer::chi_lambda_via_geck_pfeiffer`] is
/// explicitly documented as incomplete: at q ≠ 1, two basis elements
/// `T_w` and `T_{w'}` with the SAME cycle type but DIFFERENT lengths
/// give DIFFERENT Hecke characters, so the q-MN-on-cycle-type step is
/// only valid on minimal-length representatives.  The current
/// implementation reduces basis elements via simple-reflection
/// conjugation only — sufficient for many cases at n ≤ 6 but **not
/// guaranteed minimal** without the full Geck-Pfeiffer 2000 §3.2
/// "good cuspidal moves".  Empirically: D atomic braid (n=6) reduces
/// to 145 basis elements of which 17 are minimal-length and 128 are
/// not (see `geck_pfeiffer.rs` notes).
///
/// **At q = 1** the result is correct (Hecke ↦ S_n, characters are
/// class functions on cycle type alone).
///
/// **For correct q ≠ 1 evaluation on arbitrary braids**, prefer
/// [`chi_via_gp_hoefsmit`] (basis expansion + Hoefsmit per T_w —
/// correct but no MN speedup) or the direct seminormal kernel
/// [`chi_lambda_braid`] / [`chi_lambda_braid_mpfr`].
///
/// **Cost**: worst-case O(n!) basis elements but typical sparse braid
/// words give smaller spans.  At n = 6 (D atomic braid), basis can
/// have up to 720 elements but most words touch far fewer.
#[pyfunction]
fn chi_q_via_gp(
    lambda: Vec<usize>,
    n: usize,
    word: Vec<(i32, u32)>,
) -> Vec<(i32, String)> {
    let poly = geck_pfeiffer::chi_lambda_via_geck_pfeiffer(&lambda, n, &word);
    poly.terms
        .into_iter()
        .map(|(he, c)| (he, c.to_string()))
        .collect()
}

/// **Littlewood-Richardson coefficient `c^λ_{μν}`.**
///
/// Computes the multiplicity of the Specht module `S^λ` in the
/// induced representation `Ind_{S_p × S_q}^{S_n} S^μ ⊠ S^ν`, equivalently
/// the number of LR tableaux of skew shape `λ/μ` with content `ν`.
///
/// Used by the F4 composer (`chi_via_factorization`): for a tensor-
/// product factorization β = β_1 ⊗ β_2,
///
///   χ_λ(β) = Σ_{μ ⊢ p, ν ⊢ q} c^λ_{μν} · χ_μ(β_1) · χ_ν(β_2)
///
/// `lambda`: outer partition λ.
/// `mu`: inner partition μ (must satisfy μ ⊆ λ componentwise).
/// `nu`: content partition ν.
///
/// Returns 0 if `|λ| ≠ |μ| + |ν|` or μ ⊄ λ.
#[pyfunction]
fn lr_coefficient(lambda: Vec<usize>, mu: Vec<usize>, nu: Vec<usize>) -> i64 {
    littlewood_richardson::lr_coefficient(&lambda, &mu, &nu)
}

/// **Experimental q-deformed character of a braid word.**
///
/// `chi_q_word(lambda, n_strands, word)` returns a Laurent polynomial
/// as `[(half_exp, coeff_str), ...]`.  See [`mn_chi_q`] for the
/// polynomial encoding format.
///
/// **WARNING (Copilot review)**: the underlying
/// `seminormal_mn::chi_lambda_braid_qdef` is correct at `q = 1`
/// (collapses to classical MN) and on canonical/minimal-length
/// permutation braids at `q ≠ 1`, but provides a deliberately
/// simplified (and incorrect) q-deformation for non-minimal braid
/// words.  For correct q ≠ 1 evaluation on arbitrary braids, use
/// [`chi_via_gp_hoefsmit`] (basis expansion + Hoefsmit per T_w) or
/// the direct seminormal kernel [`chi_lambda_braid`].
///
/// To avoid accidental misuse this binding rejects:
///   1. Words containing negative generators (would require the
///      unsupported `σ⁻¹ = σ − h` expansion).
///   2. **Positive but non-reduced words** (Copilot review #r3144...),
///      detected by comparing word length to the underlying
///      permutation's inversion length.  E.g. `[σ_1, σ_2, σ_1]` (length
///      3) is rejected because the underlying permutation of the
///      braid `σ_1 σ_2 σ_1` is `(1 3)` with only 1 inversion → its
///      reduced expression has length 1, so the q≠1 character is NOT
///      a class function on cycle type for this 3-letter word.
#[pyfunction]
fn chi_q_word(
    lambda: Vec<usize>,
    n_strands: usize,
    word: Vec<(i32, u32)>,
) -> PyResult<Vec<(i32, String)>> {
    if word.iter().any(|(sign, _)| *sign < 0) {
        return Err(pyo3::exceptions::PyValueError::new_err(
            "chi_q_word is experimental for q != 1 and only supported \
             for canonical/minimal-length permutation braids; words \
             with negative generators are rejected. Use \
             chi_via_gp_hoefsmit or chi_lambda_braid for correct \
             evaluation on arbitrary braids.",
        ));
    }
    // Reject positive non-reduced words: the underlying permutation
    // of the braid (apply each generator on the right of the
    // identity) must have inversion-count equal to the word length.
    let mut perm: Vec<usize> = (0..n_strands).collect();
    for &(_, gen) in &word {
        let i = (gen as usize).saturating_sub(1);
        if i + 1 < perm.len() {
            perm.swap(i, i + 1);
        }
    }
    let mut inversions = 0usize;
    for i in 0..perm.len() {
        for j in (i + 1)..perm.len() {
            if perm[i] > perm[j] {
                inversions += 1;
            }
        }
    }
    if inversions != word.len() {
        return Err(pyo3::exceptions::PyValueError::new_err(format!(
            "chi_q_word: input word has length {} but its underlying \
             permutation has {} inversions — non-reduced words are not \
             supported (q-character is not a class function of cycle \
             type for non-canonical braids).  Reduce the word to a \
             minimal-length expression of the same permutation, or use \
             chi_via_gp_hoefsmit / chi_lambda_braid for correct \
             evaluation on arbitrary braids.",
            word.len(), inversions
        )));
    }
    let poly = seminormal_mn::chi_lambda_braid_qdef(&lambda, n_strands, &word);
    Ok(poly
        .terms
        .into_iter()
        .map(|(he, c)| (he, c.to_string()))
        .collect())
}

/// **q-deformed Murnaghan-Nakayama character** `χ^λ(T_w; q)` *(EXPERIMENTAL).*
///
/// Computes the Hecke character of the canonical permutation braid
/// `T_w ∈ H_n(q)` of cycle type `μ`, returning the result as a list
/// of `(half_exponent, coefficient)` pairs encoding a Laurent
/// polynomial in `q^{1/2}`.  The half-exponent `2k` represents
/// `q^{k}`; `2k+1` represents `q^{(2k+1)/2}`.
///
/// **WARNING (Copilot review #r3144...): simplified q-deformation.**
/// The underlying [`seminormal_mn::chi_lambda_mn_qdef`] is documented
/// as a deliberately-simplified Halverson–Ram-style broken-strip
/// q-deformation: at `q = 1` it agrees exactly with classical MN
/// (verified across the full S_3, S_5 character tables), and on the
/// trivial / sign irreps it agrees with Hoefsmit at `q ≠ 1`.  For
/// *non-trivial* irreps at `q ≠ 1` it is **not** the canonical
/// Ram–Wenzl q-MN — the broken-strip q-weight differs from the
/// Ram–Wenzl 1992 weight on multi-row strips.  Treat output for such
/// cases as a placeholder until the proper Ram–Wenzl recursion is
/// wired in (next milestone).
///
/// For ground truth, evaluate via the Hoefsmit kernel
/// [`chi_lambda_braid`] on a reduced word for `T_w`, or via the basis
/// expansion + Hoefsmit path [`chi_via_gp_hoefsmit`].
///
/// Currently handles permutation-form `μ` only; mixed-sign generators
/// (inverses) require Hecke-relation expansion (separate milestone).
///
/// Returns `[(half_exp, coeff_str), ...]` where `coeff_str` is the
/// BigInt rendered as decimal (callers parse via `int(s)`).
#[pyfunction]
fn mn_chi_q(lambda: Vec<usize>, mu: Vec<usize>) -> Vec<(i32, String)> {
    let poly = seminormal_mn::chi_lambda_mn_qdef(&lambda, &mu);
    poly.terms
        .into_iter()
        .map(|(he, c)| (he, c.to_string()))
        .collect()
}

/// **Batch character evaluation across many partitions** (rayon-parallel).
///
/// Evaluates `χ_λ(β)` for every partition in `shapes` in parallel using
/// Rust rayon.  Returns a `List[float]` in the same order.
///
/// Faster than calling `chi_lambda_braid` from a Python
/// `multiprocessing.Pool`: no per-partition pickling overhead, rayon
/// work-stealing balances dim variation across partitions.
#[pyfunction]
fn chi_lambdas_braid(
    shapes: Vec<Vec<usize>>,
    word: Vec<(i32, u32)>,
    q: f64,
) -> Vec<f64> {
    seminormal::chi_lambdas_braid(&shapes, &word, q)
}

/// **Batch MPFR character evaluation across many partitions** (rayon-parallel).
///
/// Like `chi_lambda_braid_mpfr` but in batch.  Returns a `List[str]`,
/// each entry being a decimal string at requested `dps` precision.
#[pyfunction]
#[pyo3(signature = (shapes, word, q_str, dps=50))]
fn chi_lambdas_braid_mpfr(
    shapes: Vec<Vec<usize>>,
    word: Vec<(i32, u32)>,
    q_str: String,
    dps: u32,
) -> Vec<String> {
    seminormal_mpfr::chi_lambdas_braid_mpfr(&shapes, &word, &q_str, dps)
}

/// **High-precision (MPFR) character `χ_λ(β)`.**
///
/// Computes the Hoefsmit seminormal character at `dps` decimal-precision
/// using MPFR-backed arbitrary-precision arithmetic. Returns the result
/// as a decimal string (callers should parse via `mpmath.mpf` or
/// equivalent). Substantially slower than the `f64` path (~10–30×) but
/// exact at the requested precision — no f64 rounding error.
///
/// `q_str`: substrate parameter as a decimal string (avoids f64 lossy
///   conversion at the boundary).
/// `dps`: requested decimal precision (default 50 if caller passes a
///   smaller value, MPFR uses internal guard bits).
#[pyfunction]
#[pyo3(signature = (shape, word, q_str, dps=50))]
fn chi_lambda_braid_mpfr(
    shape: Vec<usize>,
    word: Vec<(i32, u32)>,
    q_str: String,
    dps: u32,
) -> String {
    seminormal_mpfr::chi_lambda_braid_mpfr(&shape, &word, &q_str, dps)
}

#[pymodule]
fn pyhecke_native(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(markov_z, m)?)?;
    m.add_function(wrap_pyfunction!(hecke_h, m)?)?;
    m.add_function(wrap_pyfunction!(trace_weights, m)?)?;
    m.add_function(wrap_pyfunction!(gram_matrix, m)?)?;
    m.add_function(wrap_pyfunction!(gram_determinant, m)?)?;
    m.add_function(wrap_pyfunction!(gram_inverse, m)?)?;
    m.add_function(wrap_pyfunction!(hm, m)?)?;
    m.add_function(wrap_pyfunction!(nf_tr, m)?)?;
    m.add_function(wrap_pyfunction!(nf_net, m)?)?;
    m.add_function(wrap_pyfunction!(build_atom_nf, m)?)?;
    m.add_function(wrap_pyfunction!(atom_per_generator_volumes, m)?)?;
    m.add_function(wrap_pyfunction!(chi_lambda_braid, m)?)?;
    m.add_function(wrap_pyfunction!(chi_q_atomic, m)?)?;
    m.add_function(wrap_pyfunction!(chi_lambdas_braid, m)?)?;
    m.add_function(wrap_pyfunction!(chi_lambda_braid_mpfr, m)?)?;
    m.add_function(wrap_pyfunction!(chi_lambdas_braid_mpfr, m)?)?;
    m.add_function(wrap_pyfunction!(partitions_of, m)?)?;
    m.add_function(wrap_pyfunction!(mn_chi, m)?)?;
    m.add_function(wrap_pyfunction!(mn_chi_q, m)?)?;
    m.add_function(wrap_pyfunction!(chi_q_word, m)?)?;
    m.add_function(wrap_pyfunction!(lr_coefficient, m)?)?;
    m.add_function(wrap_pyfunction!(chi_q_via_gp, m)?)?;
    m.add_function(wrap_pyfunction!(debug_reduced_basis, m)?)?;
    m.add_function(wrap_pyfunction!(chi_via_gp_hoefsmit, m)?)?;
    m.add_function(wrap_pyfunction!(chi_lambda_all_partitions_f64, m)?)?;
    m.add_function(wrap_pyfunction!(chi_lambda_all_partitions_mpfr, m)?)?;
    m.add_function(wrap_pyfunction!(tr_m_word_lq, m)?)?;
    m.add_function(wrap_pyfunction!(tr_m_word_lq_clear_cache, m)?)?;
    m.add_function(wrap_pyfunction!(incremental_reduce_rust, m)?)?;
    // Pull __version__ directly from Cargo.toml so the Python module,
    // the Rust crate, and pyproject.toml never drift. (Gemini review
    // r3103025537: hardcoded version is fragile.)
    m.add("__version__", env!("CARGO_PKG_VERSION"))?;
    Ok(())
}

/// FFI-shaped Hecke element: `Vec<(word, Vec<(exp, num_decimal, den_decimal)>)>`.
///
/// - `word: Vec<i32>` — sequence of signed Hecke generator indices
///   (non-negative = σ_i; negative = formal variable that commutes
///   with anything, per `hecke_laurent_fast.py`'s convention).
/// - Coefficients are sparse Laurent polys in q with rational coeffs,
///   one entry per non-zero monomial: `(q-exponent, numerator-as-decimal-string,
///   denominator-as-decimal-string)`. Decimal strings preserve arbitrary
///   precision through the PyO3 boundary (mirrors the pattern used by
///   `tr_m_word_lq::to_ffi`).
type FfiHeckeElement = Vec<(Vec<i32>, Vec<(i32, String, String)>)>;

/// Incremental Hecke-element reduce in Rust. Mirrors
/// `hecke_laurent_fast.py::incremental_reduced_element_fast`:
/// start from identity, multiply factors one at a time, and reduce
/// (R1/R2/R3 fixpoint) after each multiplication.
///
/// Inputs:
/// - `factors`: list of factor elements in FFI form (see
///   `FfiHeckeElement`). Each element typically has a small number of
///   terms (one or two) — it's the σ-word representation of a single
///   crossing.
/// - `max_iterations_per_step`: per-multiplication reduce cap (matches
///   the Python `max_iterations_per_step` kwarg). Use the Python
///   default of 5000 unless you have evidence a step needs more.
///
/// Returns the reduced element in the same FFI form.
///
/// This is the Tier 1.A boundary: ONE PyO3 call per atomic-braid
/// reduction. Output is the fully-reduced Hecke element ready for
/// `tr_M_element` evaluation on the Python side.
#[pyfunction]
#[pyo3(signature = (factors, max_iterations_per_step = 5000))]
fn incremental_reduce_rust(
    factors: Vec<FfiHeckeElement>,
    max_iterations_per_step: usize,
) -> PyResult<FfiHeckeElement> {
    let mut elem = laurent_hecke_element::LaurentHeckeElement::identity();
    for (idx, raw) in factors.iter().enumerate() {
        let factor = laurent_hecke_element::LaurentHeckeElement::from_ffi(raw)
            .map_err(|msg| {
                pyo3::exceptions::PyValueError::new_err(format!(
                    "incremental_reduce_rust: factor {} parse failed: {}",
                    idx, msg
                ))
            })?;
        elem = elem.mul(&factor);
        let (reduced, _iter) =
            reduce_laurent::reduce_laurent_rules(&elem, max_iterations_per_step);
        elem = reduced;
    }
    Ok(elem.to_ffi())
}

/// Compute χ^λ(β, q) for every partition λ ⊢ n_strands, given a
/// canonical-form atomic braid word `(sign, gen_1based)` where
/// `sign ∈ {1, -1, 0}` with 0 = averaged half-sum (σ + σ⁻¹)/2.
///
/// Delegates to `hecke_engine::wenzl_lr::chi_lambda_canonical_all_partitions_f64`
/// (rayon-parallel over partitions; direct-averaging f64 path, no
/// 2^k sub-word expansion). Returns `Vec<(partition, χ^λ)>`.
///
/// Use case: the Python `markov_peel` critical path computes
/// `tr_M(β, q) = Σ_λ y_λ(q) · χ^λ(β, q)` via the Wenzl bridge.
/// The Σ_λ y_λ · χ^λ combine is cheap in Python; the per-partition
/// χ^λ at H_{3A} (A ≥ 5) is the bottleneck. This exposes the
/// Rust accelerator: dim 462 sympy matmul at H_12 → tens of ms
/// in Rust per PR #682.
#[pyfunction]
fn chi_lambda_all_partitions_f64(
    n_strands: usize,
    word: Vec<(i32, u32)>,
    q: f64,
) -> Vec<(Vec<usize>, f64)> {
    // Translate (sign, gen) → (Crossing, gen). The Rust API uses
    // `Crossing::Sigma` / `SigmaInv` / `Averaged` for sign 1/-1/0.
    let word_with_averaged: Vec<wenzl_lr::CrossingPair> = word
        .iter()
        .map(|&(sign, gen)| {
            let c = match sign {
                1 => wenzl_lr::Crossing::Sigma,
                -1 => wenzl_lr::Crossing::SigmaInv,
                0 => wenzl_lr::Crossing::Averaged,
                _ => panic!(
                    "chi_lambda_all_partitions_f64: unknown sign {} \
                     (expected -1, 0, or 1)",
                    sign
                ),
            };
            (c, gen)
        })
        .collect();
    wenzl_lr::chi_lambda_canonical_all_partitions_f64(
        n_strands,
        &word_with_averaged,
        q,
    )
}

/// **MPFR variant** of [`chi_lambda_all_partitions_f64`] at
/// arbitrary precision (≥ 50 dps recommended).
///
/// Returns `Vec<(partition, chi_decimal_string)>`. The caller is
/// expected to load each chi via `mpmath.mpf(decimal_string)` to
/// preserve precision. Per CLAUDE.md §Precision goals L1 (50-dps
/// compute floor), this is the production path for categorical
/// identities; the f64 variant exists for speed-only use cases
/// where structural-zero distinction is not required.
///
/// `q_str` is the substrate parameter as a decimal string (50+ dps
/// recommended; pin to `q_parameter.Q_50_DIGIT_STR` from Python).
/// `dps` controls the MPFR working precision (50 = production,
/// 100 = research-grade).
#[pyfunction]
fn chi_lambda_all_partitions_mpfr(
    n_strands: usize,
    word: Vec<(i32, u32)>,
    q_str: String,
    dps: u32,
) -> Vec<(Vec<usize>, String)> {
    let word_with_averaged: Vec<wenzl_lr::CrossingPair> = word
        .iter()
        .map(|&(sign, gen)| {
            let c = match sign {
                1 => wenzl_lr::Crossing::Sigma,
                -1 => wenzl_lr::Crossing::SigmaInv,
                0 => wenzl_lr::Crossing::Averaged,
                _ => panic!(
                    "chi_lambda_all_partitions_mpfr: unknown sign {} \
                     (expected -1, 0, or 1)",
                    sign
                ),
            };
            (c, gen)
        })
        .collect();
    wenzl_lr::chi_lambda_canonical_all_partitions_mpfr(
        n_strands,
        &word_with_averaged,
        &q_str,
        dps,
    )
}

/// **Markov-axiom recursive ascent** in Rust — the canonical
/// Jones-Markov trace `tr_M(w, q)` for a single Hecke word `w` in
/// H_n(q), returned as a serialised ZHLaurent polynomial in (z, h)
/// with BigInt-in-q^{1/2} coefficients.
///
/// Mirrors `folio-assistant/computations/laurent_q_trace.py
/// tr_M_word_lq` exactly, but with BigInt arithmetic in Rust
/// (no f64). Per CLAUDE.md §Precision goals L1 — every coefficient
/// is exact; the Python caller evaluates at q₀ to mpmath.mpf at
/// production dps.
///
/// `word`: 0-based generator indices (consistent with
/// `markov_trace_canonical.tr_M_word` and the Python `tr_M_word_lq`).
/// `n_strands`: H_n strand count.
///
/// Returns `Vec<((z_exp, h_exp), Vec<(q_half_exp, big_int_str)>)>`.
/// The outer Vec has one entry per non-zero (z, h) monomial; each
/// coefficient is a list of `(q_exp_doubled, BigInt_decimal_string)`
/// pairs (where `q_exp_doubled = 2 * q_exp` to support half-integer
/// q-exponents — see `hecke_engine::laurent_poly_q::LaurentPolyQ`
/// for the encoding).
///
/// Raises `RuntimeError` on Case C (multiple top-1 in segment) —
/// caller routes to the sympy ocneanu_fallback path same as the
/// Python implementation.
#[pyfunction]
fn tr_m_word_lq(
    word: Vec<u32>,
    n_strands: usize,
) -> PyResult<Vec<((i32, i32), Vec<(i32, String)>)>> {
    match rust_tr_m_word_lq::tr_m_word_lq(&word, n_strands, 200) {
        Ok(zh) => Ok(zh.to_ffi()),
        Err(msg) => Err(pyo3::exceptions::PyRuntimeError::new_err(msg)),
    }
}

/// Clear the global recursion cache. Call between independent
/// atoms to prevent unbounded memory growth in long-running
/// sessions (matches the Python `_tr_M_word_lq_cached.cache_clear()`).
#[pyfunction]
fn tr_m_word_lq_clear_cache() {
    rust_tr_m_word_lq::clear_cache();
}
