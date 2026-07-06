//! Phase-2 modular sampler for the Borromean diagonal colored-Jones
//! recurrence (bean n920; follow-up to PR #3443's existence certificate).
//!
//! Target window: the UNIQUE (nullity-1) operator at (r, W) = (6, 11):
//!
//!     sum_{i=0}^{6} a_i(q, m) J_{B,n+i} = b(q, m),   m = q^n,
//!
//! coefficients supported on m^k, |k| <= 11.  Column layout matches the
//! Python scaffold `computations/borromean_diagonal_recurrence_reconstruct.py`:
//! 7 blocks a_0..a_6 of 23 entries each (k = -11..11), then the
//! inhomogeneous block b (23 entries) — NCOLS = 8*23 = 184.
//!
//! Per prime p (CLI arg), this binary:
//!   1. samples base points s = 3, 4, ...: evaluates the Habiro tower
//!      J_{B,n} mod p (n <= 210), builds the 204-row fit system, and
//!      takes the RREF nullspace (requires nullity 1 + pivot columns
//!      EXACTLY matching the first accepted sample's; mismatches are
//!      rejected) — the canonical vector v(q) at q = s^2;
//!   2. per column c: fits v[c](q) = P_c(q)/Q_c(q) at the MINIMAL
//!      degree (bisected once per column; reusable via --degrees),
//!      validated on held-out samples, normalized canonically by
//!      making Q's leading (highest-degree) coefficient 1 — the same
//!      rational function's residues are then CRT-compatible across
//!      primes;
//!   3. prints JSON: {prime, r, W, samples, degrees, columns:
//!      [{col, P, Q}]}.
//!
//! The Python driver (computations/borromean_recurrence_crt_driver.py)
//! CRTs the residues across primes, Wang-lifts to Q, and runs the
//! claim-bearing exact symbolic annihilation in sympy.  This binary
//! alone claims nothing.

use std::env;

const R_ORD: usize = 6;
const W_WIN: i64 = 11;
const NBLK: usize = (2 * W_WIN as usize) + 1; // 23
const NCOLS: usize = (R_ORD + 2) * NBLK; // 184
const R_FIT: usize = NCOLS + 20; // 204
const NMAX: usize = R_FIT + R_ORD; // 210
const NHOLD: usize = 15;

fn mulmod(a: u64, b: u64, p: u64) -> u64 {
    ((a as u128 * b as u128) % p as u128) as u64
}

fn powmod(mut b: u64, mut e: u64, p: u64) -> u64 {
    let mut acc: u64 = 1;
    b %= p;
    while e > 0 {
        if e & 1 == 1 {
            acc = mulmod(acc, b, p);
        }
        b = mulmod(b, b, p);
        e >>= 1;
    }
    acc
}

fn inv(a: u64, p: u64) -> u64 {
    assert!(a % p != 0, "modular inverse of 0 (invalid base point)");
    powmod(a, p - 2, p)
}

/// J_{B,n} mod p for n = 1..nmax (Habiro cyclotomic sum, verified
/// transcription).  None if any bracket vanishes (bad base point).
fn jones_tower(p: u64, s: u64, nmax: usize) -> Option<Vec<u64>> {
    let top = 2 * nmax + 2;
    let sinv = inv(s, p);
    let mut br = vec![0u64; top];
    let (mut sj, mut sij) = (1u64, 1u64);
    for j in 1..top {
        sj = mulmod(sj, s, p);
        sij = mulmod(sij, sinv, p);
        br[j] = (sj + p - sij) % p;
        if br[j] == 0 {
            return None;
        }
    }
    let mut out = Vec::with_capacity(nmax);
    for n in 1..=nmax {
        let mut total: u64 = 0;
        let mut prod3: u64 = 1;
        for l in 0..n {
            if l > 0 {
                let f = mulmod(br[n + l], br[n - l], p);
                prod3 = mulmod(prod3, mulmod(f, mulmod(f, f, p), p), p);
            }
            let mut den: u64 = 1;
            for j in (l + 1)..(2 * l + 2) {
                den = mulmod(den, br[j], p);
            }
            let d2i = inv(mulmod(den, den, p), p);
            let term = mulmod(mulmod(mulmod(br[n], br[n], p), prod3, p), d2i, p);
            total = if l & 1 == 1 {
                (total + p - term) % p
            } else {
                (total + term) % p
            };
        }
        out.push(total);
    }
    Some(out)
}

/// Fit-system rows for the (6,11) window at base point s.
fn build_rows(j: &[u64], p: u64, s: u64) -> Vec<Vec<u64>> {
    let q = mulmod(s, s, p);
    let mut rows = Vec::with_capacity(R_FIT);
    for n in 1..=R_FIT {
        let m = powmod(q, n as u64, p);
        let mi = inv(m, p);
        let mut mk = vec![0u64; NBLK];
        // mk[idx] = m^(idx - W_WIN)
        mk[W_WIN as usize] = 1;
        for k in 1..=(W_WIN as usize) {
            mk[W_WIN as usize + k] = mulmod(mk[W_WIN as usize + k - 1], m, p);
            mk[W_WIN as usize - k] = mulmod(mk[W_WIN as usize - k + 1], mi, p);
        }
        let mut row = Vec::with_capacity(NCOLS);
        for i in 0..=R_ORD {
            let jni = j[n + i - 1];
            for idx in 0..NBLK {
                row.push(mulmod(mk[idx], jni, p));
            }
        }
        for idx in 0..NBLK {
            row.push(p - mk[idx]); // -m^k
        }
        rows.push(row);
    }
    rows
}

/// RREF nullspace.  Returns (basis vectors, pivot columns).
fn rref_nullspace(mut m: Vec<Vec<u64>>, p: u64) -> (Vec<Vec<u64>>, Vec<usize>) {
    let ncols = m[0].len();
    let nrows = m.len();
    let mut pivots: Vec<(usize, usize)> = Vec::new();
    let mut rank = 0usize;
    for col in 0..ncols {
        let piv = (rank..nrows).find(|&r| m[r][col] != 0);
        let piv = match piv {
            Some(r) => r,
            None => continue,
        };
        m.swap(rank, piv);
        let iv = inv(m[rank][col], p);
        for x in m[rank].iter_mut() {
            *x = mulmod(*x, iv, p);
        }
        let pivot_row = m[rank].clone();
        for (r, row) in m.iter_mut().enumerate() {
            if r != rank && row[col] != 0 {
                let f = row[col];
                for (a, b) in row.iter_mut().zip(pivot_row.iter()) {
                    *a = (*a + p - mulmod(f, *b, p)) % p;
                }
            }
        }
        pivots.push((col, rank));
        rank += 1;
        if rank == nrows {
            break;
        }
    }
    let pivot_cols: Vec<usize> = pivots.iter().map(|&(c, _)| c).collect();
    let free: Vec<usize> = (0..ncols).filter(|c| !pivot_cols.contains(c)).collect();
    let mut basis = Vec::new();
    for &fc in &free {
        let mut v = vec![0u64; ncols];
        v[fc] = 1;
        for &(c, r) in &pivots {
            v[c] = (p - m[r][fc]) % p;
        }
        basis.push(v);
    }
    (basis, pivot_cols)
}

/// Try to fit y(q) = P/Q with deg P, deg Q <= d.  Returns normalized
/// (P, Q) with Q's leading nonzero coefficient == 1, or None.
/// `require_unique`: in pinned-degree mode the fit nullspace must be
/// 1-dimensional (the minimal-degree representation is unique up to
/// scale) so that the monic-Q normalization is canonical across primes.
/// During bisection nullity > 1 at above-minimal degree is expected and
/// harmless — every null vector is (P·f, Q·f) for the SAME rational
/// function, the holdout validation rejects anything else, and the
/// bisection converges to the minimal degree anyway.
fn try_fit(
    qs: &[u64],
    ys: &[u64],
    hold_q: &[u64],
    hold_y: &[u64],
    d: usize,
    p: u64,
    require_unique: bool,
) -> Option<(Vec<u64>, Vec<u64>)> {
    let need = 2 * d + 3;
    if need > qs.len() {
        return None;
    }
    let mut rows = Vec::with_capacity(need);
    for (&qv, &yv) in qs.iter().zip(ys.iter()).take(need) {
        let mut qp = Vec::with_capacity(d + 1);
        qp.push(1u64);
        for _ in 0..d {
            let last = *qp.last().unwrap();
            qp.push(mulmod(last, qv, p));
        }
        let mut row = Vec::with_capacity(2 * d + 2);
        row.extend_from_slice(&qp);
        for &t in &qp {
            row.push(p - mulmod(yv, t, p));
        }
        rows.push(row);
    }
    let (basis, _) = rref_nullspace(rows, p);
    if basis.is_empty() || (require_unique && basis.len() != 1) {
        return None;
    }
    let v = &basis[0];
    let (pc, qc) = v.split_at(d + 1);
    if qc.iter().all(|&x| x == 0) {
        return None;
    }
    // holdout validation
    for (&qv, &yv) in hold_q.iter().zip(hold_y.iter()) {
        let mut t = 1u64;
        let (mut num, mut den) = (0u64, 0u64);
        for i in 0..=d {
            num = (num + mulmod(pc[i], t, p)) % p;
            den = (den + mulmod(qc[i], t, p)) % p;
            t = mulmod(t, qv, p);
        }
        if den == 0 || mulmod(num, inv(den, p), p) != yv {
            return None;
        }
    }
    // canonical normalization: leading (highest-degree) nonzero Q coeff = 1
    let lead_idx = (0..=d).rev().find(|&i| qc[i] != 0).unwrap();
    let li = inv(qc[lead_idx], p);
    let pn: Vec<u64> = pc.iter().map(|&x| mulmod(x, li, p)).collect();
    let qn: Vec<u64> = qc.iter().map(|&x| mulmod(x, li, p)).collect();
    Some((pn, qn))
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        eprintln!(
            "usage: {} <prime> [--samples N] [--degmax D] [--degrees d0,d1,...]",
            args[0]
        );
        std::process::exit(2);
    }
    let p: u64 = args[1].parse().expect("prime");
    let mut nsamp: usize = 640;
    let mut degmax: usize = 300;
    let mut degrees: Option<Vec<usize>> = None;
    let mut i = 2;
    while i < args.len() {
        match args[i].as_str() {
            "--samples" => {
                nsamp = args[i + 1].parse().unwrap();
                i += 2;
            }
            "--degmax" => {
                degmax = args[i + 1].parse().unwrap();
                i += 2;
            }
            "--degrees" => {
                let dv: Vec<usize> = args[i + 1]
                    .split(',')
                    .map(|x| x.parse().unwrap())
                    .collect();
                if dv.len() != NCOLS {
                    eprintln!("--degrees needs {} entries, got {}", NCOLS, dv.len());
                    std::process::exit(2);
                }
                degrees = Some(dv);
                i += 2;
            }
            _ => {
                eprintln!("unknown arg {}", args[i]);
                std::process::exit(2);
            }
        }
    }

    // ── Stage 1: sample canonical null vectors ─────────────────────────
    let mut qs: Vec<u64> = Vec::new();
    let mut vals: Vec<Vec<u64>> = vec![Vec::new(); NCOLS];
    let mut pivots_ref: Option<Vec<usize>> = None;
    let mut s: u64 = 2;
    let mut rejected = 0usize;
    while qs.len() < nsamp {
        s += 1;
        let j = match jones_tower(p, s, NMAX) {
            Some(j) => j,
            None => continue,
        };
        let rows = build_rows(&j, p, s);
        let (basis, piv) = rref_nullspace(rows, p);
        if basis.len() != 1 {
            rejected += 1;
            continue;
        }
        match &pivots_ref {
            None => pivots_ref = Some(piv),
            Some(pr) => {
                if *pr != piv {
                    rejected += 1;
                    continue;
                }
            }
        }
        qs.push(mulmod(s, s, p));
        for (c, slot) in vals.iter_mut().enumerate() {
            slot.push(basis[0][c]);
        }
        if qs.len() % 80 == 0 {
            eprintln!("[stage1] {}/{} samples (s={}, rejected={})", qs.len(), nsamp, s, rejected);
        }
    }
    let (fit_q, hold_q) = qs.split_at(qs.len() - NHOLD);

    // ── Stage 2: per-column minimal-degree fits ────────────────────────
    let mut deg_out: Vec<usize> = Vec::with_capacity(NCOLS);
    let mut cols_json: Vec<String> = Vec::with_capacity(NCOLS);
    for c in 0..NCOLS {
        let ys = &vals[c];
        let (fit_y, hold_y) = ys.split_at(ys.len() - NHOLD);
        if ys.iter().all(|&x| x == 0) {
            deg_out.push(0);
            cols_json.push(format!("{{\"col\":{},\"P\":[0],\"Q\":[1]}}", c));
            continue;
        }
        let fit = match &degrees {
            Some(dv) => try_fit(fit_q, fit_y, hold_q, hold_y, dv[c], p, true),
            None => {
                // bisect the minimal fitting degree in [0, degmax]
                let (mut lo, mut hi, mut found) = (0usize, degmax, None);
                if let Some(f) = try_fit(fit_q, fit_y, hold_q, hold_y, hi, p, false) {
                    found = Some((hi, f));
                } else {
                    eprintln!("[stage2] col {}: NO FIT at degmax {}", c, degmax);
                    std::process::exit(1);
                }
                while hi - lo > 1 {
                    let mid = (lo + hi) / 2;
                    match try_fit(fit_q, fit_y, hold_q, hold_y, mid, p, false) {
                        Some(f) => {
                            hi = mid;
                            found = Some((mid, f));
                        }
                        None => lo = mid,
                    }
                }
                found.map(|(_, f)| f)
            }
        };
        let (pn, qn) = match fit {
            Some(f) => f,
            None => {
                eprintln!("[stage2] col {}: fit failed at pinned degree", c);
                std::process::exit(1);
            }
        };
        deg_out.push(pn.len() - 1);
        let pj: Vec<String> = pn.iter().map(|x| x.to_string()).collect();
        let qj: Vec<String> = qn.iter().map(|x| x.to_string()).collect();
        cols_json.push(format!(
            "{{\"col\":{},\"P\":[{}],\"Q\":[{}]}}",
            c,
            pj.join(","),
            qj.join(",")
        ));
        if c % 20 == 0 {
            eprintln!("[stage2] col {}/{} done (deg {})", c, NCOLS, deg_out[c]);
        }
    }

    let degs: Vec<String> = deg_out.iter().map(|x| x.to_string()).collect();
    println!(
        "{{\"prime\":{},\"r\":{},\"W\":{},\"samples\":{},\"degrees\":[{}],\"columns\":[{}]}}",
        p,
        R_ORD,
        W_WIN,
        qs.len(),
        degs.join(","),
        cols_json.join(",")
    );
}
