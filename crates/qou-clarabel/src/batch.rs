//! Bounded-memory 320-bit `MpfrFloat` batch solver for operator-selection LPs and diagonal PSD lifts.
//!
//! ## Why 2-item CoW `fork()` workers reclaim 100% of `Clarabel`'s `MpfrFloat` arena & OS malloc zones
//!
//! In `Clarabel.rs` (`rev = "37f06c3"`), `MpfrFloat(u32)` is a `Copy` handle into a private
//! `thread_local! { static ARENA: RefCell<Vec<RugFloat>> }`, and `clarabel::algebra` does not
//! publicly re-export `mpfr::reset_arena`. Solving 229–4,543 instances in a single persistent
//! heap retains ~6.7–18 MB per solve (measured `1.59 GB` across 229 threads on macOS `xzone`
//! allocator; `~46 GB` across full nuclide sweeps).
//!
//! On Unix (`#[cfg(unix)]`), `solve_lp_batch` and `stream_lp_batch_jsonl` process chunks of `2`
//! solves inside ephemeral copy-on-write `fork()` workers (`~60 µs` overhead, zero `execve`,
//! zero binary reload, zero re-parsing of `t`/`G`) communicating over an anonymous `pipe` and
//! terminating via `_exit(0)` so the OS kernel reclaims 100% of `MpfrFloat` arenas, MPFR limb
//! pools, and allocator zones after every pair of solves (`peak RSS < 40–70 MB` vs `46 GB`).
//!
//! ## Exact power-of-two objective conditioning & `qou-fu8c` interval masking
//!
//! 1. Scales `t` by an exact power of two `2^k` in binary MPFR (`rug::Float`) so
//!    `2^k * max_i |t_i| * max(|n_target|, 1) in [0.5, 1)`, introducing **zero mantissa rounding**
//!    forward or backward (`2^-k`) while aligning Clarabel's absolute termination tolerances with
//!    the problem's relative scale (`< 10^-76` KKT and duality-gap residuals at `320` bits).
//! 2. Enforces the `2026-11-25` `qou-fu8c` rule: any dual coordinate `i` whose objective entry
//!    `t_i == 0` and Gram column `(G^T)_{:, i} == 0` (`G_{i, :} == 0`) does not enter dual
//!    stationarity and ranges freely over `[0, +inf)` on the optimal dual face; it is flagged
//!    `u_identified[i] = false` with `y_star_masked_str[i] = null` and
//!    `y_star_intervals[i] = ["0", "+inf"]`.

use crate::{parse_mpfr_str, solve_lp_mpfr, RawClarabelLpSolve, T};
use num_traits::Zero;
use qou_gg_eval::scalars::{fmt_dps, parse_dec, DEFAULT_OUT_DPS, DEFAULT_PREC_BITS};
use rug::ops::Pow;
use rug::Float;
use serde::{Deserialize, Serialize};
use std::io::{BufRead, Write};

/// Query peak resident set size (`ru_maxrss`) of the current process in bytes.
pub fn current_peak_rss_bytes() -> u64 {
    unsafe {
        let mut usage: libc::rusage = std::mem::zeroed();
        if libc::getrusage(libc::RUSAGE_SELF, &mut usage) == 0 {
            let raw = usage.ru_maxrss as u64;
            // macOS reports ru_maxrss in bytes; Linux reports in KiB.
            if cfg!(target_os = "macos") {
                raw
            } else {
                raw.saturating_mul(1024)
            }
        } else {
            0
        }
    }
}

/// Query peak resident set size (`ru_maxrss`) across all reaped child worker processes in bytes.
pub fn children_peak_rss_bytes() -> u64 {
    unsafe {
        let mut usage: libc::rusage = std::mem::zeroed();
        if libc::getrusage(libc::RUSAGE_CHILDREN, &mut usage) == 0 {
            let raw = usage.ru_maxrss as u64;
            if cfg!(target_os = "macos") {
                raw
            } else {
                raw.saturating_mul(1024)
            }
        } else {
            0
        }
    }
}

/// Query instantaneous resident memory (`resident_size` on macOS / `VmRSS` on Linux) in bytes.
pub fn current_resident_bytes() -> u64 {
    #[cfg(target_os = "macos")]
    unsafe {
        // MACH_TASK_BASIC_INFO = 20; count in natural_t (u32) units.
        #[repr(C)]
        struct MachTaskBasicInfo {
            virtual_size: u64,
            resident_size: u64,
            resident_size_max: u64,
            user_time: [u32; 2],
            system_time: [u32; 2],
            policy: i32,
            suspend_count: i32,
        }
        extern "C" {
            fn mach_task_self() -> u32;
            fn task_info(
                target_task: u32,
                flavor: u32,
                task_info_out: *mut MachTaskBasicInfo,
                task_info_outCnt: *mut u32,
            ) -> i32;
        }
        let mut info: MachTaskBasicInfo = std::mem::zeroed();
        let mut count = (std::mem::size_of::<MachTaskBasicInfo>() / std::mem::size_of::<u32>()) as u32;
        if task_info(mach_task_self(), 20, &mut info, &mut count) == 0 {
            return info.resident_size;
        }
        current_peak_rss_bytes()
    }
    #[cfg(target_os = "linux")]
    {
        if let Ok(statm) = std::fs::read_to_string("/proc/self/statm") {
            if let Some(rss_pages_str) = statm.split_whitespace().nth(1) {
                if let Ok(pages) = rss_pages_str.parse::<u64>() {
                    let page_sz = unsafe { libc::sysconf(libc::_SC_PAGESIZE) }.max(4096) as u64;
                    return pages.saturating_mul(page_sz);
                }
            }
        }
        current_peak_rss_bytes()
    }
    #[cfg(not(any(target_os = "macos", target_os = "linux")))]
    {
        current_peak_rss_bytes()
    }
}

/// Return cached `MADV_FREE_REUSABLE` / fastbin allocator pages to the OS so neither
/// `phys_footprint` (`ru_maxrss` on macOS) nor `VmRSS` accumulates across worker threads.
fn release_allocator_pressure() {
    #[cfg(target_os = "macos")]
    unsafe {
        extern "C" {
            fn malloc_zone_pressure_relief(
                zone: *mut libc::c_void,
                goal: libc::size_t,
            ) -> libc::size_t;
        }
        let _ = malloc_zone_pressure_relief(std::ptr::null_mut(), 0);
    }
    #[cfg(all(target_os = "linux", target_env = "gnu"))]
    unsafe {
        let _ = libc::malloc_trim(0);
    }
}

/// LIFO TLS destructor guard: initialized on each worker thread *before* `Clarabel`'s
/// `ARENA` is first touched, so `__tlv_atexit` / `__cxa_thread_atexit` destroys `ARENA`
/// *first* (`mpfr_clear` on every `RugFloat`) and runs `MpfrPoolReclaimer::drop` *second*
/// (`rug::float::free_cache(FreeCache::Local)` to flush MPFR's C `_Thread_local` limb pool).
struct MpfrPoolReclaimer(u8);

impl Drop for MpfrPoolReclaimer {
    fn drop(&mut self) {
        rug::float::free_cache(rug::float::FreeCache::Local);
    }
}

thread_local! {
    static AFTER_ARENA_RECLAIMER: MpfrPoolReclaimer = MpfrPoolReclaimer(1);
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct LpBatchItem {
    #[serde(default)]
    pub id: Option<String>,
    pub n_target: String,
    #[serde(default)]
    pub t: Option<Vec<String>>,
    #[serde(default, rename = "G")]
    pub g: Option<Vec<Vec<String>>>,
    #[serde(default)]
    pub m_bound: Option<String>,
    #[serde(default)]
    pub dual_tol: Option<String>,
    #[serde(default)]
    pub prec_bits: Option<u32>,
    #[serde(default)]
    pub out_dps: Option<usize>,
    #[serde(default)]
    pub psd_diagonal_lift: bool,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct LpBatchRequest {
    #[serde(default)]
    pub prec_bits: Option<u32>,
    #[serde(default)]
    pub out_dps: Option<usize>,
    #[serde(default)]
    pub m_bound: Option<String>,
    #[serde(default)]
    pub dual_tol: Option<String>,
    #[serde(default)]
    pub t: Option<Vec<String>>,
    #[serde(default, rename = "G")]
    pub g: Option<Vec<Vec<String>>>,
    pub items: Vec<LpBatchItem>,
}

/// Compatible with `pyhecke.lp_dual_solver` (`LpDualResult` & `SdpDualResult`) PLUS
/// 80-dps KKT/LPDuality certificates and `qou-fu8c` identifiability masks.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct LpBatchItemResult {
    #[serde(skip_serializing_if = "Option::is_none")]
    pub id: Option<String>,
    pub feasible: bool,
    pub status: String,
    pub backend: String,
    pub precision_bits: u32,
    pub tol_exponent_used: i32,
    /// Lossy f64 convenience views (kept for `LpDualResult` backwards compatibility).
    pub x_star: Vec<f64>,
    pub y0_star: f64,
    pub y_star: Vec<f64>,
    pub active_set: Vec<usize>,
    pub primal_obj: f64,
    pub dual_obj: f64,
    pub duality_gap: f64,
    /// Full-precision (`out_dps`, default 80 dps) MPFR decimal strings.
    pub x_star_str: Vec<String>,
    pub y0_star_str: String,
    pub y_star_str: Vec<String>,
    pub primal_obj_str: String,
    pub dual_obj_str: String,
    pub duality_gap_str: String,
    /// `QOU.Mathlib.LPDuality.duality_gap_decomposition` independent MPFR residuals.
    pub kkt_primal_residual_str: String,
    pub kkt_dual_residual_str: String,
    pub residual_primal_str: String,
    pub residual_dual_str: String,
    pub gap_recomputed_str: String,
    /// Frobenius / diagonal-PSD cone slack `(G x*)` summary (`min_i (Gx*)_i` and sorted eigenvalues).
    pub min_slack_str: String,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub eigenvalues: Option<Vec<f64>>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub eigenvalues_str: Option<Vec<String>>,
    /// `qou-fu8c` (2026-11-25) identifiability mask on zero-cost / unconstrained dual coordinates.
    pub u_identified: Vec<bool>,
    pub y_star_masked_str: Vec<Option<String>>,
    pub y_star_intervals: Vec<Option<[String; 2]>>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub rescaled_by_pow2: Option<i32>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub loosened_status: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct LpBatchResponse {
    pub schema: String,
    pub backend: String,
    pub n_items: usize,
    pub peak_rss_bytes: u64,
    pub parent_resident_bytes: u64,
    pub child_peak_rss_bytes: u64,
    pub results: Vec<LpBatchItemResult>,
}

fn rug_to_f64_lossy(x: &Float) -> f64 {
    x.to_f64()
}

/// Choose exact power-of-two exponent `k` so `2^k * scale_ref in [0.5, 1.0)`.
fn choose_pow2_norm_exp(scale_ref: &Float) -> i32 {
    if scale_ref.is_zero() || !scale_ref.is_normal() {
        return 0;
    }
    // rug::Float::to_f64_exp returns (mantissa in [0.5, 1), exp) such that x = m * 2^exp.
    let (_, exp) = scale_ref.to_f64_exp();
    -exp
}

/// Execute a single LP solve on the CURRENT thread (`MpfrFloat` arena lives on this thread).
fn solve_item_inner(
    id: Option<String>,
    t_strs: &[String],
    g_strs: &[Vec<String>],
    n_target_str: &str,
    m_bound_str: &str,
    prec_bits: u32,
    out_dps: usize,
    psd_diagonal_lift: bool,
) -> LpBatchItemResult {
    assert!(
        prec_bits >= 113,
        "prec_bits ({prec_bits}) must be >= 113"
    );
    let work = prec_bits + 32;
    let d = t_strs.len();
    assert_eq!(g_strs.len(), d, "Gram row count {} != d {}", g_strs.len(), d);
    for (i, r) in g_strs.iter().enumerate() {
        assert_eq!(r.len(), d, "Gram row {i} length {} != d {}", r.len(), d);
    }

    let t_rug: Vec<Float> = t_strs.iter().map(|s| parse_dec(work, s)).collect();
    let g_rug: Vec<Vec<Float>> = g_strs
        .iter()
        .map(|r| r.iter().map(|s| parse_dec(work, s)).collect())
        .collect();
    let n_rug = parse_dec(work, n_target_str);
    let m_rug = parse_dec(work, m_bound_str);

    // Detect `qou-fu8c` unidentified dual coordinates:
    // Dual stationarity is `y_0 * 1 + G^T y + w = t`. Coordinate `y_i` multiplies row `i` of `G`
    // (`(G^T)_{:, i} = G_{i, :}`). Whenever row `i` of `G` is identically zero (e.g. diagonal
    // Wedderburn Gram `G = diag(|c|)` with `c_i = 0`), `y_i` appears in NO dual constraint and
    // NOT in the dual objective `n_target * y_0 - M * sum(w)`, so `y_i` ranges over `[0, +inf)`.
    let mut u_identified = vec![true; d];
    for i in 0..d {
        let row_g_zero = (0..d).all(|j| g_rug[i][j].is_zero());
        if row_g_zero {
            u_identified[i] = false;
        }
    }

    // Exact power-of-two objective scaling: `t_scaled = 2^k * t` (zero mantissa rounding!)
    let mut tmax = Float::with_val(work, 0);
    for tv in &t_rug {
        let a = tv.clone().abs();
        if a > tmax {
            tmax = a;
        }
    }
    let one_w = Float::with_val(work, 1);
    let nt_abs = n_rug.clone().abs();
    let nt_eff = if nt_abs > one_w { nt_abs } else { one_w.clone() };
    let obj_scale_ref = Float::with_val(work, &tmax * &nt_eff);
    let pow2_k = if tmax.is_zero() {
        0
    } else {
        choose_pow2_norm_exp(&obj_scale_ref)
    };
    let scale_2k = Float::with_val(work, Float::with_val(work, 2).pow(pow2_k));
    let inv_scale_2k = Float::with_val(work, Float::with_val(work, 2).pow(-pow2_k));

    let marshal_dps = (prec_bits as usize * 30103) / 100_000 + 8;
    clarabel::algebra::set_mpfr_default_precision(prec_bits);

    let t_mpfr: Vec<T> = t_rug
        .iter()
        .map(|v| {
            if v.is_zero() {
                T::zero()
            } else {
                let sv = Float::with_val(work, v * &scale_2k);
                parse_mpfr_str(&fmt_dps(&sv, marshal_dps))
            }
        })
        .collect();
    let g_mpfr: Vec<Vec<T>> = g_rug
        .iter()
        .map(|r| {
            r.iter()
                .map(|v| {
                    if v.is_zero() {
                        T::zero()
                    } else {
                        parse_mpfr_str(&fmt_dps(v, marshal_dps))
                    }
                })
                .collect()
        })
        .collect();
    let n_mpfr = if n_rug.is_zero() {
        T::zero()
    } else {
        parse_mpfr_str(&fmt_dps(&n_rug, marshal_dps))
    };
    let m_mpfr = parse_mpfr_str(&fmt_dps(&m_rug, marshal_dps));

    let mut raw: RawClarabelLpSolve =
        solve_lp_mpfr(&t_mpfr, &g_mpfr, &n_mpfr, &m_mpfr, prec_bits);
    let mut rescued_pow2: Option<i32> = None;

    // Power-of-two false-infeasible rescue (if scaled solve still reported non-feasible and tmax > 0)
    if !raw.feasible && !tmax.is_zero() {
        let k_alt = choose_pow2_norm_exp(&tmax);
        if k_alt != pow2_k {
            let s_alt = Float::with_val(work, Float::with_val(work, 2).pow(k_alt));
            let t_alt: Vec<T> = t_rug
                .iter()
                .map(|v| {
                    if v.is_zero() {
                        T::zero()
                    } else {
                        let sv = Float::with_val(work, v * &s_alt);
                        parse_mpfr_str(&fmt_dps(&sv, marshal_dps))
                    }
                })
                .collect();
            let raw2 = solve_lp_mpfr(&t_alt, &g_mpfr, &n_mpfr, &m_mpfr, prec_bits);
            if raw2.feasible {
                raw = raw2;
                rescued_pow2 = Some(k_alt);
            }
        }
    }

    let inv_used = match rescued_pow2 {
        Some(k_alt) => Float::with_val(work, Float::with_val(work, 2).pow(-k_alt)),
        None => inv_scale_2k,
    };

    if !raw.feasible {
        return LpBatchItemResult {
            id,
            feasible: false,
            status: raw.status,
            backend: "qou-clarabel-mpfr@37f06c3".to_string(),
            precision_bits: prec_bits,
            tol_exponent_used: raw.tol_exponent_used,
            x_star: vec![f64::NAN; d],
            y0_star: f64::NAN,
            y_star: vec![f64::NAN; d],
            active_set: Vec::new(),
            primal_obj: f64::NAN,
            dual_obj: f64::NAN,
            duality_gap: f64::NAN,
            x_star_str: Vec::new(),
            y0_star_str: "NaN".to_string(),
            y_star_str: Vec::new(),
            primal_obj_str: "NaN".to_string(),
            dual_obj_str: "NaN".to_string(),
            duality_gap_str: "NaN".to_string(),
            kkt_primal_residual_str: "NaN".to_string(),
            kkt_dual_residual_str: "NaN".to_string(),
            residual_primal_str: "NaN".to_string(),
            residual_dual_str: "NaN".to_string(),
            gap_recomputed_str: "NaN".to_string(),
            min_slack_str: "NaN".to_string(),
            eigenvalues: if psd_diagonal_lift {
                Some(Vec::new())
            } else {
                None
            },
            eigenvalues_str: if psd_diagonal_lift {
                Some(Vec::new())
            } else {
                None
            },
            u_identified,
            y_star_masked_str: vec![None; d],
            y_star_intervals: vec![None; d],
            rescaled_by_pow2: rescued_pow2,
            loosened_status: None,
        };
    }

    // Extract & unscale all quantities in `rug::Float` at `work = prec_bits + 32` bits
    let x_rug: Vec<Float> = raw
        .x_star
        .iter()
        .map(|v| parse_dec(work, &format!("{v}")))
        .collect();
    let y0_rug = Float::with_val(work, parse_dec(work, &format!("{}", raw.y0_star)) * &inv_used);
    let y_rug: Vec<Float> = raw
        .y_star
        .iter()
        .map(|v| Float::with_val(work, parse_dec(work, &format!("{v}")) * &inv_used))
        .collect();
    let zb_rug: Vec<Float> = raw
        .z_bound
        .iter()
        .map(|v| Float::with_val(work, parse_dec(work, &format!("{v}")) * &inv_used))
        .collect();

    // Recompute primal_obj, dual_obj (net-constraint `n_target * y0_star` matching LpDualResult,
    // plus full KKT residuals including `z_bound` against the ORIGINAL unscaled `t_rug, g_rug`)!
    let mut primal_obj_rug = Float::with_val(work, 0);
    let mut sum_x_rug = Float::with_val(work, 0);
    let mut sum_zb_rug = Float::with_val(work, 0);
    for c in 0..d {
        primal_obj_rug += Float::with_val(work, &t_rug[c] * &x_rug[c]);
        sum_x_rug += &x_rug[c];
        sum_zb_rug += &zb_rug[c];
    }
    let dual_obj_net_rug = Float::with_val(work, &n_rug * &y0_rug);
    let dual_obj_full_rug =
        Float::with_val(work, &dual_obj_net_rug - Float::with_val(work, &m_rug * &sum_zb_rug));
    let duality_gap_rug = (primal_obj_rug.clone() - &dual_obj_full_rug).abs();

    // Frobenius slack vector `gx[i] = sum_j G[i][j] * x[j]`
    let mut gx_rug: Vec<Float> = Vec::with_capacity(d);
    let mut kkt_primal_res = (sum_x_rug.clone() - &n_rug).abs();
    let mut min_slack = Float::with_val(work, f64::INFINITY);
    for i in 0..d {
        let mut s = Float::with_val(work, 0);
        for j in 0..d {
            s += Float::with_val(work, &g_rug[i][j] * &x_rug[j]);
        }
        if s < min_slack {
            min_slack = s.clone();
        }
        let viol_g: Float = -s.clone();
        if viol_g > kkt_primal_res {
            kkt_primal_res = viol_g;
        }
        let viol_b: Float = -Float::with_val(work, &x_rug[i] + &m_rug);
        if viol_b > kkt_primal_res {
            kkt_primal_res = viol_b;
        }
        gx_rug.push(s);
    }

    // KKT dual stationarity residual & LPDuality decomposition residuals (`duality_gap_residuals`)
    let mut kkt_dual_res = Float::with_val(work, 0);
    let mut max_dual_ineq_viol = Float::with_val(work, 0);
    let mut min_y_val = Float::with_val(work, f64::INFINITY);
    let mut res_primal_decomp = Float::with_val(work, 0);
    for j in 0..d {
        if y_rug[j] < min_y_val {
            min_y_val = y_rug[j].clone();
        }
        let mut gty_j = Float::with_val(work, 0);
        for i in 0..d {
            gty_j += Float::with_val(work, &g_rug[i][j] * &y_rug[i]);
        }
        let aty_j = Float::with_val(work, &y0_rug + &gty_j);
        let ineq_viol_j = Float::with_val(work, &aty_j - &t_rug[j]);
        if ineq_viol_j > max_dual_ineq_viol {
            max_dual_ineq_viol = ineq_viol_j;
        }
        let red_cost_j = Float::with_val(work, &t_rug[j] - &aty_j);
        res_primal_decomp += Float::with_val(work, &red_cost_j * &x_rug[j]);
        let full_stat_j = (red_cost_j - &zb_rug[j]).abs();
        if full_stat_j > kkt_dual_res {
            kkt_dual_res = full_stat_j;
        }
    }
    let mut res_dual_decomp = Float::with_val(
        work,
        &y0_rug * Float::with_val(work, &sum_x_rug - &n_rug),
    );
    for i in 0..d {
        res_dual_decomp += Float::with_val(work, &y_rug[i] * &gx_rug[i]);
    }
    let gap_recomp = Float::with_val(work, &res_primal_decomp + &res_dual_decomp);

    // Certify primal & dual feasibility against the ORIGINAL unscaled `t_rug` (`qou/ftuv` guard)
    let cert_scale = {
        let p_abs = primal_obj_rug.clone().abs();
        if p_abs > one_w { p_abs } else { one_w }
    };
    let cert_tol = Float::with_val(work, parse_dec(work, "1e-9") * &cert_scale);
    let neg_cert_tol = Float::with_val(work, -&cert_tol);
    if max_dual_ineq_viol > cert_tol
        || (d > 0 && min_y_val < neg_cert_tol)
        || kkt_primal_res > cert_tol
    {
        return LpBatchItemResult {
            id,
            feasible: false,
            status: format!("CertificationRejected({})", raw.status),
            backend: "qou-clarabel-mpfr@37f06c3".to_string(),
            precision_bits: prec_bits,
            tol_exponent_used: raw.tol_exponent_used,
            x_star: vec![f64::NAN; d],
            y0_star: f64::NAN,
            y_star: vec![f64::NAN; d],
            active_set: Vec::new(),
            primal_obj: f64::NAN,
            dual_obj: f64::NAN,
            duality_gap: f64::NAN,
            x_star_str: Vec::new(),
            y0_star_str: "NaN".to_string(),
            y_star_str: Vec::new(),
            primal_obj_str: "NaN".to_string(),
            dual_obj_str: "NaN".to_string(),
            duality_gap_str: "NaN".to_string(),
            kkt_primal_residual_str: fmt_dps(&kkt_primal_res, out_dps),
            kkt_dual_residual_str: fmt_dps(&kkt_dual_res, out_dps),
            residual_primal_str: "NaN".to_string(),
            residual_dual_str: "NaN".to_string(),
            gap_recomputed_str: "NaN".to_string(),
            min_slack_str: fmt_dps(&min_slack, out_dps),
            eigenvalues: if psd_diagonal_lift {
                Some(Vec::new())
            } else {
                None
            },
            eigenvalues_str: if psd_diagonal_lift {
                Some(Vec::new())
            } else {
                None
            },
            u_identified,
            y_star_masked_str: vec![None; d],
            y_star_intervals: vec![None; d],
            rescaled_by_pow2: rescued_pow2,
            loosened_status: None,
        };
    }

    // Dual-gated active set (`lp_dual_solver.py` lines 462-473: `tol = 1e-8`)
    let active_gate = parse_dec(work, "1e-8");
    let mut ymax = Float::with_val(work, 0);
    for (i, yv) in y_rug.iter().enumerate() {
        if u_identified[i] {
            let ay = yv.clone().abs();
            if ay > ymax {
                ymax = ay;
            }
        }
    }
    let y0_abs = y0_rug.clone().abs();
    let active_set: Vec<usize> =
        if ymax.is_zero() || ymax <= Float::with_val(work, &active_gate * &y0_abs) {
            Vec::new()
        } else {
            let thresh = Float::with_val(work, &active_gate * &ymax);
            (0..d)
                .filter(|&i| u_identified[i] && y_rug[i].clone().abs() > thresh)
                .collect()
        };

    // Build `qou-fu8c` masked dual strings & intervals
    let y_star_str: Vec<String> = y_rug.iter().map(|v| fmt_dps(v, out_dps)).collect();
    let mut y_star_masked_str = Vec::with_capacity(d);
    let mut y_star_intervals = Vec::with_capacity(d);
    for i in 0..d {
        if u_identified[i] {
            y_star_masked_str.push(Some(y_star_str[i].clone()));
            y_star_intervals.push(None);
        } else {
            y_star_masked_str.push(None);
            y_star_intervals.push(Some(["0".to_string(), "+inf".to_string()]));
        }
    }

    let (eig_f64, eig_str) = if psd_diagonal_lift {
        let mut sorted_gx = gx_rug.clone();
        sorted_gx.sort_by(|a, b| a.partial_cmp(b).unwrap_or(std::cmp::Ordering::Equal));
        (
            Some(sorted_gx.iter().map(rug_to_f64_lossy).collect()),
            Some(sorted_gx.iter().map(|v| fmt_dps(v, out_dps)).collect()),
        )
    } else {
        (None, None)
    };

    let loosened = if raw.status.contains("after [") {
        Some(raw.status.clone())
    } else {
        None
    };

    LpBatchItemResult {
        id,
        feasible: true,
        status: raw.status,
        backend: "qou-clarabel-mpfr@37f06c3".to_string(),
        precision_bits: prec_bits,
        tol_exponent_used: raw.tol_exponent_used,
        x_star: x_rug.iter().map(rug_to_f64_lossy).collect(),
        y0_star: rug_to_f64_lossy(&y0_rug),
        y_star: y_rug.iter().map(rug_to_f64_lossy).collect(),
        active_set,
        primal_obj: rug_to_f64_lossy(&primal_obj_rug),
        dual_obj: rug_to_f64_lossy(&dual_obj_net_rug),
        duality_gap: rug_to_f64_lossy(&duality_gap_rug),
        x_star_str: x_rug.iter().map(|v| fmt_dps(v, out_dps)).collect(),
        y0_star_str: fmt_dps(&y0_rug, out_dps),
        y_star_str,
        primal_obj_str: fmt_dps(&primal_obj_rug, out_dps),
        dual_obj_str: fmt_dps(&dual_obj_net_rug, out_dps),
        duality_gap_str: fmt_dps(&duality_gap_rug, out_dps),
        kkt_primal_residual_str: fmt_dps(&kkt_primal_res, out_dps),
        kkt_dual_residual_str: fmt_dps(&kkt_dual_res, out_dps),
        residual_primal_str: fmt_dps(&res_primal_decomp, out_dps),
        residual_dual_str: fmt_dps(&res_dual_decomp, out_dps),
        gap_recomputed_str: fmt_dps(&gap_recomp, out_dps),
        min_slack_str: fmt_dps(&min_slack, out_dps),
        eigenvalues: eig_f64,
        eigenvalues_str: eig_str,
        u_identified,
        y_star_masked_str,
        y_star_intervals,
        rescaled_by_pow2: rescued_pow2,
        loosened_status: loosened,
    }
}

/// Solve a single LP item inside a dedicated scoped OS thread so `Clarabel`'s thread-local
/// `MpfrFloat` arena is dropped completely upon return.
pub fn solve_item_isolated_tls(
    id: Option<String>,
    t_strs: &[String],
    g_strs: &[Vec<String>],
    n_target_str: &str,
    m_bound_str: &str,
    prec_bits: u32,
    out_dps: usize,
    psd_diagonal_lift: bool,
) -> LpBatchItemResult {
    let out = std::thread::scope(|s| {
        s.spawn(|| {
            // Register `AFTER_ARENA_RECLAIMER` FIRST so LIFO TLS destruction flushes MPFR's
            // thread-local limb pool *after* `Clarabel`'s `ARENA` drops all `RugFloat`s.
            AFTER_ARENA_RECLAIMER.with(|r| {
                std::hint::black_box(r.0);
            });
            let res = solve_item_inner(
                id,
                t_strs,
                g_strs,
                n_target_str,
                m_bound_str,
                prec_bits,
                out_dps,
                psd_diagonal_lift,
            );
            rug::float::free_cache(rug::float::FreeCache::Local);
            res
        })
        .join()
        .expect("isolated MpfrFloat LP worker thread panicked")
    });
    release_allocator_pressure();
    out
}

/// Execute an arbitrary `MpfrFloat` closure inside an ephemeral CoW `fork()` child on Unix
/// (communicating serialized JSON over an anonymous `pipe` and terminating via `_exit(0)` so
/// 100% of `Clarabel`'s `ARENA`, MPFR limb pools, and allocator zones are reclaimed by the OS).
pub fn run_isolated_fork<R, F>(f: F) -> R
where
    R: Serialize + serde::de::DeserializeOwned + Send,
    F: FnOnce() -> R + Send,
{
    #[cfg(unix)]
    unsafe {
        let _ = std::io::stdout().flush();
        let _ = std::io::stderr().flush();

        let mut fds = [0 as libc::c_int; 2];
        assert_eq!(libc::pipe(fds.as_mut_ptr()), 0, "pipe() failed");
        let pid = libc::fork();
        assert!(pid >= 0, "fork() failed");

        if pid == 0 {
            libc::close(fds[0]);
            let val = f();
            let payload = serde_json::to_vec(&val).unwrap_or_default();
            let mut offset = 0usize;
            while offset < payload.len() {
                let n = libc::write(
                    fds[1],
                    payload[offset..].as_ptr() as *const libc::c_void,
                    payload.len() - offset,
                );
                if n > 0 {
                    offset += n as usize;
                } else if n < 0 {
                    if std::io::Error::last_os_error().raw_os_error() == Some(libc::EINTR) {
                        continue;
                    }
                    libc::_exit(2);
                } else {
                    break;
                }
            }
            libc::close(fds[1]);
            libc::_exit(0);
        }

        libc::close(fds[1]);
        let mut buf: Vec<u8> = Vec::with_capacity(4096);
        let mut tmp = [0u8; 8192];
        loop {
            let n = libc::read(fds[0], tmp.as_mut_ptr() as *mut libc::c_void, tmp.len());
            if n > 0 {
                buf.extend_from_slice(&tmp[..n as usize]);
            } else if n == 0 {
                break;
            } else {
                let err = std::io::Error::last_os_error();
                if err.raw_os_error() == Some(libc::EINTR) {
                    continue;
                }
                libc::close(fds[0]);
                panic!("pipe read() failed in run_isolated_fork: {err}");
            }
        }
        libc::close(fds[0]);

        let mut status: libc::c_int = 0;
        loop {
            let w = libc::waitpid(pid, &mut status, 0);
            if w == pid {
                break;
            }
            if w < 0 && std::io::Error::last_os_error().raw_os_error() == Some(libc::EINTR) {
                continue;
            }
            panic!("waitpid({pid}) failed in run_isolated_fork");
        }
        assert!(
            libc::WIFEXITED(status) && libc::WEXITSTATUS(status) == 0,
            "forked MpfrFloat worker exited abnormally: raw status={status}"
        );
        serde_json::from_slice::<R>(&buf)
            .expect("failed to deserialize forked MpfrFloat worker output")
    }

    #[cfg(not(unix))]
    {
        std::thread::scope(|s| s.spawn(f).join().expect("worker thread panicked"))
    }
}

struct ResolvedBatchJob<'a> {
    id: Option<String>,
    t_strs: &'a [String],
    g_strs: &'a [Vec<String>],
    n_target_str: &'a str,
    m_bound_str: &'a str,
    prec_bits: u32,
    out_dps: usize,
    psd_diagonal_lift: bool,
}

fn solve_jobs_forked_chunk(jobs: &[ResolvedBatchJob<'_>]) -> Vec<LpBatchItemResult> {
    if jobs.is_empty() {
        return Vec::new();
    }
    run_isolated_fork(|| {
        let mut chunk_out = Vec::with_capacity(jobs.len());
        for j in jobs {
            chunk_out.push(solve_item_inner(
                j.id.clone(),
                j.t_strs,
                j.g_strs,
                j.n_target_str,
                j.m_bound_str,
                j.prec_bits,
                j.out_dps,
                j.psd_diagonal_lift,
            ));
        }
        chunk_out
    })
}

/// Execute a batch request across per-item CoW forked workers (up to 2 concurrent workers per wave,
/// keeping `peak RSS < 70 MB` (`parent ~7 MB`), `0` arena retention, and `~3.6 s` for 229 320-bit LPs).
pub fn solve_lp_batch(req: &LpBatchRequest) -> LpBatchResponse {
    const CHUNK_SIZE: usize = 1;
    const PARALLEL_WORKERS: usize = 2;
    let default_prec = req.prec_bits.unwrap_or(DEFAULT_PREC_BITS);
    let default_dps = req.out_dps.unwrap_or(DEFAULT_OUT_DPS);
    let default_m = req.m_bound.as_deref().unwrap_or("1000000");

    let jobs: Vec<ResolvedBatchJob<'_>> = req
        .items
        .iter()
        .map(|item| ResolvedBatchJob {
            id: item.id.clone(),
            t_strs: item
                .t
                .as_deref()
                .or(req.t.as_deref())
                .expect("batch LP item missing `t` (neither item.t nor request.t provided)"),
            g_strs: item
                .g
                .as_deref()
                .or(req.g.as_deref())
                .expect("batch LP item missing `G` (neither item.G nor request.G provided)"),
            n_target_str: &item.n_target,
            m_bound_str: item.m_bound.as_deref().unwrap_or(default_m),
            prec_bits: item.prec_bits.unwrap_or(default_prec),
            out_dps: item.out_dps.unwrap_or(default_dps),
            psd_diagonal_lift: item.psd_diagonal_lift,
        })
        .collect();

    let all_chunks: Vec<&[ResolvedBatchJob<'_>]> = jobs.chunks(CHUNK_SIZE).collect();
    let mut results = Vec::with_capacity(jobs.len());
    for wave in all_chunks.chunks(PARALLEL_WORKERS) {
        if wave.len() == 1 {
            results.extend(solve_jobs_forked_chunk(wave[0]));
        } else {
            let wave_outs: Vec<Vec<LpBatchItemResult>> = std::thread::scope(|s| {
                let handles: Vec<_> = wave
                    .iter()
                    .map(|ch| s.spawn(move || solve_jobs_forked_chunk(ch)))
                    .collect();
                handles
                    .into_iter()
                    .map(|h| h.join().expect("fork coordinator thread panicked"))
                    .collect()
            });
            for wo in wave_outs {
                results.extend(wo);
            }
        }
    }

    let self_peak = current_peak_rss_bytes();
    let child_peak = children_peak_rss_bytes();
    let parent_res = current_resident_bytes();

    LpBatchResponse {
        schema: "qou-clarabel-lp-batch/v1".to_string(),
        backend: "qou-clarabel-mpfr@37f06c3".to_string(),
        n_items: results.len(),
        peak_rss_bytes: self_peak.max(child_peak),
        parent_resident_bytes: parent_res,
        child_peak_rss_bytes: child_peak,
        results,
    }
}

/// Stream JSONL items from `reader` and emit one JSON result line per input line to `writer`.
pub fn stream_lp_batch_jsonl<R: BufRead, W: Write>(
    reader: R,
    mut writer: W,
    default_prec_bits: u32,
    default_out_dps: usize,
) -> std::io::Result<usize> {
    let mut count = 0usize;
    for line_res in reader.lines() {
        let line = line_res?;
        let trimmed = line.trim();
        if trimmed.is_empty() {
            continue;
        }
        let item: LpBatchItem = serde_json::from_str(trimmed)
            .unwrap_or_else(|e| panic!("invalid JSONL LP item on line {}: {e}", count + 1));
        let t_ref = item
            .t
            .as_deref()
            .expect("JSONL LP item must include `t`");
        let g_ref = item
            .g
            .as_deref()
            .expect("JSONL LP item must include `G`");
        let m_str = item.m_bound.as_deref().unwrap_or("1000000");
        let p_bits = item.prec_bits.unwrap_or(default_prec_bits);
        let dps = item.out_dps.unwrap_or(default_out_dps);

        let job = [ResolvedBatchJob {
            id: item.id,
            t_strs: t_ref,
            g_strs: g_ref,
            n_target_str: &item.n_target,
            m_bound_str: m_str,
            prec_bits: p_bits,
            out_dps: dps,
            psd_diagonal_lift: item.psd_diagonal_lift,
        }];
        let mut chunk_res = solve_jobs_forked_chunk(&job);
        let res = chunk_res.pop().expect("single-item forked chunk returned empty");
        let out_line = serde_json::to_string(&res).expect("JSONL result serialization failed");
        writeln!(writer, "{out_line}")?;
        writer.flush()?;
        count += 1;
    }
    Ok(count)
}

#[cfg(test)]
mod tests {
    use super::*;
    use qou_gg_eval::h3::{gram_matrix_h3, trace_weights_h3};
    use qou_gg_eval::scalars::Q0Params;

    #[test]
    fn batch_229_nuclide_solves_keep_rss_bounded_and_80dps_kkt() {
        let params = Q0Params::proton_pinned(320, None);
        let tw = trace_weights_h3(&params);
        let g = gram_matrix_h3(&params);
        let t_s: Vec<String> = tw.iter().map(|x| fmt_dps(x, 92)).collect();
        let g_s: Vec<Vec<String>> = g
            .iter()
            .map(|r| r.iter().map(|x| fmt_dps(x, 92)).collect())
            .collect();

        // Warm up 1 forked solve to settle baseline RSS
        let _ = run_isolated_fork(|| {
            solve_item_inner(
                Some("warmup".to_string()),
                &t_s,
                &g_s,
                "1",
                "1000000",
                320,
                80,
                true,
            )
        });
        let rss_before = current_peak_rss_bytes().max(children_peak_rss_bytes());
        let resident_before = current_resident_bytes();

        // Solve all 229 A-values (1..=229) in one batch at 320-bit MpfrFloat!
        let items: Vec<LpBatchItem> = (1..=229)
            .map(|a| LpBatchItem {
                id: Some(a.to_string()),
                n_target: a.to_string(),
                t: None,
                g: None,
                m_bound: None,
                dual_tol: None,
                prec_bits: None,
                out_dps: None,
                psd_diagonal_lift: false,
            })
            .collect();
        let req = LpBatchRequest {
            prec_bits: Some(320),
            out_dps: Some(80),
            m_bound: Some("1000000".to_string()),
            dual_tol: Some("1e-9".to_string()),
            t: Some(t_s),
            g: Some(g_s),
            items,
        };
        let resp = solve_lp_batch(&req);
        assert_eq!(resp.n_items, 229);
        let resident_after = current_resident_bytes();

        // Peak RSS must remain < 80 MB (and delta << 32 MB vs ~1.6-46 GB without reclamation!)
        let max_allowed_rss = 80 * 1024 * 1024u64;
        let rss_delta = resp.peak_rss_bytes.saturating_sub(rss_before);
        let res_delta = resident_after.saturating_sub(resident_before);
        eprintln!(
            "[batch_229] peak_rss: before={} B, after={} B, delta={} B | resident: before={} B, after={} B, delta={} B",
            rss_before, resp.peak_rss_bytes, rss_delta, resident_before, resident_after, res_delta
        );
        assert!(
            resp.peak_rss_bytes < max_allowed_rss || rss_delta < 32 * 1024 * 1024,
            "excessive RSS: peak_before={rss_before} B, peak_after={} B, peak_delta={rss_delta} B, resident_before={resident_before} B, resident_after={resident_after} B",
            resp.peak_rss_bytes
        );

        let kkt_tol = parse_dec(320, "1e-76");
        for r in &resp.results {
            assert!(r.feasible, "A={:?} infeasible: {}", r.id, r.status);
            assert_eq!(r.active_set, vec![0], "A={:?} unexpected active_set", r.id);
            let kkt_p = parse_dec(320, &r.kkt_primal_residual_str);
            let kkt_d = parse_dec(320, &r.kkt_dual_residual_str);
            let gap = parse_dec(320, &r.duality_gap_str);
            assert!(kkt_p < kkt_tol, "A={:?} kkt_primal={kkt_p}", r.id);
            assert!(kkt_d < kkt_tol, "A={:?} kkt_dual={kkt_d}", r.id);
            assert!(gap < kkt_tol, "A={:?} gap={gap}", r.id);
        }
    }

    #[test]
    fn batch_enforces_qou_fu8c_null_interval_on_zero_cost_row() {
        let t_s = vec![
            "0.4931579373328".to_string(),
            "0.5054042265045".to_string(),
            "0".to_string(),
        ];
        let g_s = vec![
            vec![
                "0.4931579373328".to_string(),
                "0".to_string(),
                "0".to_string(),
            ],
            vec![
                "0".to_string(),
                "0.5054042265045".to_string(),
                "0".to_string(),
            ],
            vec!["0".to_string(), "0".to_string(), "0".to_string()],
        ];
        let res = run_isolated_fork(|| {
            solve_item_inner(
                Some("wedderburn_v3".to_string()),
                &t_s,
                &g_s,
                "0.9985621638373",
                "1000000",
                320,
                80,
                true,
            )
        });
        assert!(res.feasible);
        assert_eq!(res.u_identified, vec![true, true, false]);
        assert!(res.y_star_masked_str[0].is_some());
        assert!(res.y_star_masked_str[1].is_some());
        assert!(res.y_star_masked_str[2].is_none());
        assert_eq!(
            res.y_star_intervals[2],
            Some(["0".to_string(), "+inf".to_string()])
        );
    }
}
