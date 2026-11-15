//! Convention-D Markov trace of the v9 nuclear element, past A = 16.
//!
//! Rust/MPFR port of `computations/probes/markov_trace_two_row_tower_probe.py`
//! (bean `qou-m7py`, PR #7728), rearranged so that memory is O(d) instead of
//! O(sum d^2).
//!
//! # The element
//!
//! For a nucleus with Z protons and N neutrons (A = Z + N strands, protons
//! first), v9 builds
//!
//! ```text
//!   E = prod_{k=1}^{A-1} prod_{i=0}^{k-1} f(type_i, type_k; sigma_i)
//! ```
//!
//! multiplied left to right in that order, with
//!
//! ```text
//!   p-p : sigma_i
//!   n-n : sigma_i - h      (= sigma_i^{-1})
//!   p-n : (2 sigma_i - h)  (stored doubled; the result is divided by 2^pn)
//! ```
//!
//! and `h = q - 1/q`, `sigma^2 = h sigma + 1`.
//!
//! # The trace
//!
//! Under convention D (`z = q^3/(q^2+1)`) every shape with a third row has
//! weight zero, so
//!
//! ```text
//!   tr(x) = sum_k  [n-2k+1]_q / [2]_q^n  *  chi_(n-k,k)(x).
//! ```
//!
//! # Why columns, not matrices
//!
//! The Python probe keeps the full matrices of every two-row irrep and walks
//! them up the tower. That needs `sum_k d_k^2 = Catalan(A)` numbers:
//! 3.5e7 at A = 16, but 1.8e9 at A = 19 and 6.6e9 at A = 20. At MPFR
//! precision that is far beyond memory. Here the character is instead
//! `chi(E) = sum_j (E e_j)_j`, and each `E e_j` is computed by applying the
//! factors to one vector in reverse order. Every factor `a + b sigma_i` is
//! sparse (each basis vector couples to at most one partner in Young's
//! seminormal basis), so one column costs O(L d) with L = A(A-1)/2 factors.
//! Memory is O(d) per thread. The total work is O(L * Catalan(A)), the same
//! order as the matrix walk at the top level, and it is embarrassingly
//! parallel over columns.
//!
//! # Precision
//!
//! MPFR via `rug` throughout; `q0` is read from its 50-digit decimal string,
//! never from an f64. No f64 enters the arithmetic. Output is printed to 60
//! significant digits, matching the `tr_markov_d` certificate field.
//!
//! # Self-checks (run before every computation)
//!
//! On every two-row irrep with n <= 6: `sigma^2 = h sigma + 1`, the braid
//! relation, `tr(1) = 1`, `tr(sigma_1 ... sigma_{n-1}) = z^{n-1}`,
//! `tr(sigma_0 sigma_1 sigma_0) = h z^2 + z`.
//!
//! Usage:
//!   two-row-tower-trace <Z> <N> [--prec BITS] [--threads T] [--out FILE]
//!                       [--checkpoint FILE] [--chunk COLS]
//!
//! With `--checkpoint`, the columns run in chunks of `COLS` (default 2000) and
//! each finished chunk's exact sum is appended to FILE; rerunning the same
//! command resumes after the last finished chunk.

use rayon::prelude::*;
use rug::ops::Pow;
use rug::{Assign, Float};
use std::sync::atomic::{AtomicU64, Ordering};
use std::time::Instant;

const Q0_STR: &str = "1.1099785827513808075916690956107688798744991218736";

// ---------------------------------------------------------------- tableaux

/// All two-row standard tableaux with `n` boxes, grouped by k = row-2 length.
/// A tableau is a vector of rows (0 or 1) for entries 0..n, in the same
/// generation order as the Python probe.
fn tableaux(n: usize) -> Vec<Vec<Vec<u8>>> {
    let mut out: Vec<Vec<Vec<u8>>> = vec![vec![vec![]]];
    for m in 0..n {
        let mut nxt: Vec<Vec<Vec<u8>>> = vec![Vec::new(); out.len() + 1];
        for (k, tabs) in out.iter().enumerate() {
            let r1 = m - k;
            for t in tabs {
                let mut a = t.clone();
                a.push(0);
                nxt[k].push(a);
                if k + 1 <= r1 {
                    let mut b = t.clone();
                    b.push(1);
                    nxt[k + 1].push(b);
                }
            }
        }
        while nxt.last().map_or(false, |v| v.is_empty()) {
            nxt.pop();
        }
        out = nxt;
    }
    out
}

fn contents(t: &[u8]) -> Vec<i64> {
    let mut rowlen = [0i64, 0i64];
    let mut c = Vec::with_capacity(t.len());
    for &r in t {
        c.push(rowlen[r as usize] - r as i64);
        rowlen[r as usize] += 1;
    }
    c
}

/// One generator's action on one irrep: for each basis index, either a
/// diagonal eigenvalue (axial distance +-1) or a partner and the axial
/// distance r > 0 of the oriented pair.
#[derive(Clone)]
enum Slot {
    Diag { plus: bool },
    PairHead { partner: usize, r: usize },
    PairTail,
}

struct Irrep {
    n: usize,
    k: usize,
    dim: usize,
    /// `gens[i][j]`: action of sigma_i on basis vector j.
    gens: Vec<Vec<Slot>>,
}

impl Irrep {
    fn new(n: usize, k: usize, tabs: &[Vec<u8>]) -> Irrep {
        let dim = tabs.len();
        let index: std::collections::HashMap<&[u8], usize> =
            tabs.iter().enumerate().map(|(j, t)| (t.as_slice(), j)).collect();
        let cont: Vec<Vec<i64>> = tabs.iter().map(|t| contents(t)).collect();
        let mut gens = Vec::with_capacity(n.saturating_sub(1));
        for i in 0..n.saturating_sub(1) {
            let mut slots: Vec<Option<Slot>> = vec![None; dim];
            for j in 0..dim {
                if slots[j].is_some() {
                    continue;
                }
                let r = cont[j][i + 1] - cont[j][i];
                if r.abs() == 1 {
                    slots[j] = Some(Slot::Diag { plus: r == 1 });
                    continue;
                }
                let mut t2 = tabs[j].clone();
                t2.swap(i, i + 1);
                let j2 = index[t2.as_slice()];
                let (head, tail, rr) = if r > 0 { (j, j2, r) } else { (j2, j, -r) };
                slots[head] = Some(Slot::PairHead { partner: tail, r: rr as usize });
                slots[tail] = Some(Slot::PairTail);
            }
            gens.push(slots.into_iter().map(|s| s.unwrap()).collect());
        }
        Irrep { n, k, dim, gens }
    }
}

// ------------------------------------------------------------- coefficients

/// Coefficients of one factor `a + b sigma` on one irrep level `n`:
/// eigen-scalars for the diagonal slots, and for each axial distance r >= 2
/// the 2x2 block acting on (x_head, x_tail).
struct FactorCoeffs {
    s_plus: Float,
    s_minus: Float,
    /// `blk[r] = (c11, c12, c21, c22)`:
    /// new_head = c11 x_head + c12 x_tail ; new_tail = c21 x_head + c22 x_tail.
    blk: Vec<(Float, Float, Float, Float)>,
}

fn alpha(q: &Float, r: i64, prec: u32) -> Float {
    // (q - 1/q) / (1 - q^(-2r))
    let h = Float::with_val(prec, q - Float::with_val(prec, q.recip_ref()));
    let qp = Float::with_val(prec, q.clone().pow((-2 * r) as i32));
    let den = Float::with_val(prec, 1 - qp);
    Float::with_val(prec, h / den)
}

fn factor_coeffs(q: &Float, a: &Float, b: &Float, nmax: usize, prec: u32) -> FactorCoeffs {
    let qi = Float::with_val(prec, q.recip_ref());
    let s_plus = Float::with_val(prec, a + Float::with_val(prec, b * q));
    let s_minus = Float::with_val(prec, a - Float::with_val(prec, b * &qi));
    let mut blk = Vec::with_capacity(nmax + 1);
    for r in 0..=nmax {
        if r < 2 {
            let z = Float::with_val(prec, 0);
            blk.push((z.clone(), z.clone(), z.clone(), z));
            continue;
        }
        let ar = alpha(q, r as i64, prec);
        let am = alpha(q, -(r as i64), prec);
        let c = Float::with_val(prec, 1 + Float::with_val(prec, &ar * &am));
        let c11 = Float::with_val(prec, a + Float::with_val(prec, b * &ar));
        let c12 = Float::with_val(prec, b * &c);
        let c21 = b.clone();
        let c22 = Float::with_val(prec, a + Float::with_val(prec, b * &am));
        blk.push((c11, c12, c21, c22));
    }
    FactorCoeffs { s_plus, s_minus, blk }
}

/// v <- rho(a + b sigma_i) v, in place, using two scratch Floats.
fn apply(rep: &Irrep, i: usize, fc: &FactorCoeffs, v: &mut [Float], t1: &mut Float, t2: &mut Float) {
    for (j, slot) in rep.gens[i].iter().enumerate() {
        match slot {
            Slot::Diag { plus } => {
                let s = if *plus { &fc.s_plus } else { &fc.s_minus };
                v[j] *= s;
            }
            Slot::PairHead { partner, r } => {
                let (c11, c12, c21, c22) = &fc.blk[*r];
                let jt = *partner;
                {
                    let (x, y) = (&v[j], &v[jt]);
                    t1.assign(c11 * x + c12 * y);
                    t2.assign(c21 * x + c22 * y);
                }
                std::mem::swap(&mut v[j], t1);
                std::mem::swap(&mut v[jt], t2);
            }
            Slot::PairTail => {}
        }
    }
}

fn qint(q: &Float, m: i64, prec: u32) -> Float {
    let num = Float::with_val(prec, Float::with_val(prec, q.clone().pow(m as i32)) - Float::with_val(prec, q.clone().pow((-m) as i32)));
    let den = Float::with_val(prec, q - Float::with_val(prec, q.recip_ref()));
    Float::with_val(prec, num / den)
}

fn weight(q: &Float, n: usize, k: usize, prec: u32) -> Float {
    let num = qint(q, (n - 2 * k + 1) as i64, prec);
    let den = Float::with_val(prec, qint(q, 2, prec).clone().pow(n as i32));
    Float::with_val(prec, num / den)
}

/// The factor list `(i, kind)` of the v9 element, in product order.
/// kind: 0 = pp, 1 = nn, 2 = pn.
fn v9_factors(z: usize, n: usize) -> (Vec<(usize, u8)>, u32) {
    let a = z + n;
    let mut out = Vec::new();
    let mut pn = 0u32;
    for k in 1..a {
        for i in 0..k {
            let pi = i < z;
            let pk = k < z;
            let kind = match (pi, pk) {
                (true, true) => 0,
                (false, false) => 1,
                _ => {
                    pn += 1;
                    2
                }
            };
            out.push((i, kind));
        }
    }
    (out, pn)
}

/// Weighted character sum `sum_k w_k chi_k(prod factors)` at level `nlev`,
/// for an arbitrary factor list, column by column, in parallel.
fn trace_of_word(
    q: &Float,
    nlev: usize,
    factors: &[(usize, Float, Float)],
    prec: u32,
    progress: bool,
    ckpt: Option<&Checkpoint>,
) -> Float {
    let tabs = tableaux(nlev);
    let reps: Vec<Irrep> = tabs.iter().enumerate().map(|(k, t)| Irrep::new(nlev, k, t)).collect();
    let coeffs: Vec<FactorCoeffs> =
        factors.iter().map(|(_, a, b)| factor_coeffs(q, a, b, nlev + 1, prec)).collect();
    let weights: Vec<Float> = (0..reps.len()).map(|k| weight(q, nlev, k, prec)).collect();
    let jobs: Vec<(usize, usize)> =
        reps.iter().enumerate().flat_map(|(k, r)| (0..r.dim).map(move |j| (k, j))).collect();
    let total = jobs.len() as u64;
    let work_per_col: Vec<u64> = reps.iter().map(|r| (r.dim as u64) * factors.len() as u64).collect();
    let total_work: u64 = reps.iter().map(|r| (r.dim as u64) * (r.dim as u64)).sum::<u64>()
        * factors.len() as u64;
    let done_cols = AtomicU64::new(0);
    let done_work = AtomicU64::new(0);
    let t0 = Instant::now();
    let last = std::sync::Mutex::new(Instant::now());
    if progress {
        eprintln!(
            "level {nlev}: irrep dims {:?}, columns {total}, factor applications x dim = {total_work:.3e}",
            reps.iter().map(|r| r.dim).collect::<Vec<_>>(),
            total_work = total_work as f64 // display only
        );
    }
    // Chunks run in order; each finished chunk's exact sum is appended to the
    // checkpoint, so a killed run resumes at the first unfinished chunk.
    let chunk = ckpt.map_or(jobs.len().max(1), |c| c.chunk);
    let done_chunks = ckpt.map_or_else(Vec::new, |c| c.load(prec));
    let mut sum = Float::with_val(prec, 0);
    let mut resumed_work: u64 = 0;
    for (ci, part) in jobs.chunks(chunk).enumerate() {
        if let Some(s) = done_chunks.get(ci) {
            sum += s;
            let c = done_cols.fetch_add(part.len() as u64, Ordering::Relaxed);
            let w: u64 = part.iter().map(|&(k, _)| work_per_col[k]).sum();
            done_work.fetch_add(w, Ordering::Relaxed);
            resumed_work += w;
            if progress && ci + 1 == done_chunks.len() {
                eprintln!("  resumed: {} chunks ({} cols) from checkpoint", ci + 1, c + part.len() as u64);
            }
            continue;
        }
        let part_sum = part
            .par_iter()
            .map(|&(k, j)| {
                let rep = &reps[k];
                let mut v: Vec<Float> = (0..rep.dim).map(|_| Float::with_val(prec, 0)).collect();
                v[j].assign(1);
                let mut t1 = Float::with_val(prec, 0);
                let mut t2 = Float::with_val(prec, 0);
                for (fi, (i, _, _)) in factors.iter().enumerate().rev() {
                    apply(rep, *i, &coeffs[fi], &mut v, &mut t1, &mut t2);
                }
                let c = done_cols.fetch_add(1, Ordering::Relaxed) + 1;
                let w = done_work.fetch_add(work_per_col[k], Ordering::Relaxed) + work_per_col[k];
                if progress {
                    let mut l = last.lock().unwrap();
                    if l.elapsed().as_secs() >= 10 || c == total {
                        *l = Instant::now();
                        let el = t0.elapsed().as_secs_f64();
                        let frac = w as f64 / total_work as f64; // display only
                        // ETA from the work done in THIS process, not the resumed part.
                        let fresh = (w - resumed_work) as f64 / (total_work - resumed_work) as f64;
                        let eta = if fresh > 0.0 { el / fresh - el } else { 0.0 };
                        eprintln!(
                            "  [{c}/{total} cols, {:.1}% work] elapsed {el:.0}s eta {eta:.0}s",
                            100.0 * frac
                        );
                    }
                }
                Float::with_val(prec, &v[j] * &weights[k])
            })
            .reduce(|| Float::with_val(prec, 0), |a, b| Float::with_val(prec, a + b));
        if let Some(c) = ckpt {
            c.append(ci, &part_sum);
        }
        sum += &part_sum;
    }
    sum
}

/// Append-only checkpoint: a header line fixing the run, then one line per
/// finished chunk, `<index> <exact base-16 MPFR value> end`.
struct Checkpoint {
    path: String,
    header: String,
    chunk: usize,
}

impl Checkpoint {
    fn load(&self, prec: u32) -> Vec<Float> {
        let Ok(text) = std::fs::read_to_string(&self.path) else {
            std::fs::write(&self.path, format!("{}\n", self.header)).unwrap();
            return Vec::new();
        };
        let mut lines = text.lines();
        let head = lines.next().unwrap_or("");
        assert!(head == self.header, "checkpoint {} is for a different run: {head:?}", self.path);
        let mut out = Vec::new();
        let mut kept = vec![head.to_string()];
        for l in lines {
            // Every complete line ends in " end"; a torn line (killed mid-write)
            // can still parse as a shorter hex number, so the marker, not the
            // parse, decides completeness. Torn and later lines are dropped.
            let Some(body) = l.strip_suffix(" end") else { break };
            let Some((i, v)) = body.split_once(' ') else { break };
            let (Ok(i), Ok(v)) = (i.parse::<usize>(), Float::parse_radix(v, 16)) else { break };
            if i != out.len() {
                break;
            }
            out.push(Float::with_val(prec, v));
            kept.push(l.to_string());
        }
        // Rewrite with only the complete lines, so appends start on a clean line.
        std::fs::write(&self.path, kept.join("\n") + "\n").unwrap();
        out
    }

    fn append(&self, ci: usize, v: &Float) {
        use std::io::Write;
        let mut f = std::fs::OpenOptions::new().append(true).open(&self.path).unwrap();
        writeln!(f, "{ci} {} end", v.to_string_radix(16, None)).unwrap();
        f.sync_all().unwrap();
    }
}

// ------------------------------------------------------------- self-checks

fn self_check(q: &Float, prec: u32) -> Float {
    let h = Float::with_val(prec, q - Float::with_val(prec, q.recip_ref()));
    let q3 = Float::with_val(prec, q.clone().pow(3));
    let zd = Float::with_val(prec, &q3 / Float::with_val(prec, Float::with_val(prec, q.clone().pow(2)) + 1));
    let zero = Float::with_val(prec, 0);
    let one = Float::with_val(prec, 1);
    let mut worst = Float::with_val(prec, 0);
    let mut upd = |x: Float| {
        let ax = Float::with_val(prec, x.abs_ref());
        if ax > worst {
            worst = ax;
        }
    };
    for n in 2..=6usize {
        let tabs = tableaux(n);
        for (k, t) in tabs.iter().enumerate() {
            let rep = Irrep::new(n, k, t);
            let sig = factor_coeffs(q, &zero, &one, n + 1, prec);
            let quad = factor_coeffs(q, &one, &h, n + 1, prec);
            let mut t1 = Float::with_val(prec, 0);
            let mut t2 = Float::with_val(prec, 0);
            for j in 0..rep.dim {
                let e = |j: usize| -> Vec<Float> {
                    let mut v: Vec<Float> = (0..rep.dim).map(|_| Float::with_val(prec, 0)).collect();
                    v[j].assign(1);
                    v
                };
                for i in 0..n - 1 {
                    // sigma^2 e_j = (1 + h sigma) e_j
                    let mut a = e(j);
                    apply(&rep, i, &sig, &mut a, &mut t1, &mut t2);
                    apply(&rep, i, &sig, &mut a, &mut t1, &mut t2);
                    let mut b = e(j);
                    apply(&rep, i, &quad, &mut b, &mut t1, &mut t2);
                    for (x, y) in a.iter().zip(b.iter()) {
                        upd(Float::with_val(prec, x - y));
                    }
                }
                for i in 0..n.saturating_sub(2) {
                    let mut a = e(j);
                    for g in [i, i + 1, i] {
                        apply(&rep, g, &sig, &mut a, &mut t1, &mut t2);
                    }
                    let mut b = e(j);
                    for g in [i + 1, i, i + 1] {
                        apply(&rep, g, &sig, &mut b, &mut t1, &mut t2);
                    }
                    for (x, y) in a.iter().zip(b.iter()) {
                        upd(Float::with_val(prec, x - y));
                    }
                }
            }
        }
        // tr(1) = 1
        let tr1 = trace_of_word(q, n, &[], prec, false, None);
        upd(Float::with_val(prec, &tr1 - 1));
        // tr(sigma_1 ... sigma_{n-1}) = z^{n-1}  (indices 0..n-2)
        let chain: Vec<(usize, Float, Float)> =
            (0..n - 1).map(|i| (i, zero.clone(), one.clone())).collect();
        let trc = trace_of_word(q, n, &chain, prec, false, None);
        upd(Float::with_val(prec, &trc - Float::with_val(prec, zd.clone().pow((n - 1) as i32))));
        if n >= 3 {
            let w: Vec<(usize, Float, Float)> =
                [0usize, 1, 0].iter().map(|&i| (i, zero.clone(), one.clone())).collect();
            let t3 = trace_of_word(q, n, &w, prec, false, None);
            let rhs = Float::with_val(
                prec,
                Float::with_val(prec, &h * Float::with_val(prec, zd.clone().pow(2))) + &zd,
            );
            upd(Float::with_val(prec, &t3 - &rhs));
        }
    }
    worst
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let mut pos = Vec::new();
    let mut prec: u32 = 300;
    let mut threads: usize = 4;
    let mut out: Option<String> = None;
    let mut ckpt_path: Option<String> = None;
    let mut chunk: usize = 2000;
    let mut it = args.iter().skip(1);
    while let Some(a) = it.next() {
        match a.as_str() {
            "--prec" => prec = it.next().unwrap().parse().unwrap(),
            "--threads" => threads = it.next().unwrap().parse().unwrap(),
            "--out" => out = Some(it.next().unwrap().clone()),
            "--checkpoint" => ckpt_path = Some(it.next().unwrap().clone()),
            "--chunk" => chunk = it.next().unwrap().parse().unwrap(),
            _ => pos.push(a.clone()),
        }
    }
    if pos.len() != 2 {
        eprintln!("usage: two-row-tower-trace <Z> <N> [--prec BITS] [--threads T] [--out FILE] [--checkpoint FILE] [--chunk COLS]");
        std::process::exit(2);
    }
    let z: usize = pos[0].parse().unwrap();
    let n: usize = pos[1].parse().unwrap();
    rayon::ThreadPoolBuilder::new().num_threads(threads).build_global().unwrap();
    let q = Float::with_val(prec, Float::parse(Q0_STR).unwrap());
    let t0 = Instant::now();

    let worst = self_check(&q, prec);
    let tol = Float::with_val(prec, Float::with_val(prec, 2).clone().pow(-(prec as i32) + 40));
    eprintln!("self-check (Hecke, braid, Markov, sigma0 sigma1 sigma0): worst residual {}",
        worst.to_string_radix(10, Some(6)));
    assert!(worst < tol, "representation self-check failed");

    let a = z + n;
    let h = Float::with_val(prec, &q - Float::with_val(prec, q.recip_ref()));
    let (fl, pn) = v9_factors(z, n);
    let factors: Vec<(usize, Float, Float)> = fl
        .iter()
        .map(|&(i, kind)| match kind {
            0 => (i, Float::with_val(prec, 0), Float::with_val(prec, 1)),
            1 => (i, Float::with_val(prec, -&h), Float::with_val(prec, 1)),
            _ => (i, Float::with_val(prec, -&h), Float::with_val(prec, 2)),
        })
        .collect();
    eprintln!("Z={z} N={n} A={a}: {} factors, pn={pn}, prec={prec} bits, threads={threads}",
        factors.len());
    let ck = ckpt_path.map(|path| Checkpoint {
        path,
        header: format!("two-row-tower-trace Z={z} N={n} prec={prec} chunk={chunk} q0={Q0_STR}"),
        chunk,
    });
    let tr = trace_of_word(&q, a, &factors, prec, true, ck.as_ref());
    let two_pn = Float::with_val(prec, Float::with_val(prec, 2).clone().pow(pn as i32));
    let val = Float::with_val(prec, &tr / &two_pn);
    let s = val.to_string_radix(10, Some(60));
    let el = t0.elapsed().as_secs_f64();
    println!("Z={z} N={n} A={a} pn={pn} tr_markov_d={s} elapsed={el:.1}s");
    if let Some(path) = out {
        let json = serde_json::json!({
            "q0": Q0_STR,
            "z": "q^3/(q^2+1)",
            "method": "two-row seminormal characters, column-by-column (two-row-tower-trace, Rust/MPFR)",
            "prec_bits": prec,
            "threads": threads,
            "self_check_worst_residual": worst.to_string_radix(10, Some(6)),
            "Z": z, "N": n, "A": a, "pn": pn,
            "tr_markov_d": s,
            "elapsed_seconds": el,
            "argv": args,
        });
        std::fs::write(&path, serde_json::to_string_pretty(&json).unwrap()).unwrap();
    }
}
