// v9: BigInt symbolic engine — no i128 overflow.
//
// Drop-in replacement for v8 using num-bigint for coefficients.
// Target: A=60 (⁶⁰Co) in symbolic q with mid-crossing stripping.
//
// Key differences from v8:
// 1. LPoly coefficients are BigInt (arbitrary precision)
// 2. Mid-crossing stripping always on (threshold configurable)
// 3. Iterative quotienting: reuse color content from A=n for A=n+1
// 4. Memory-bounded: strip aggressively to stay under budget
//
// Usage:
//   hecke-bigint Z N [mid_strip_threshold]
//   e.g. hecke-bigint 27 33 10000   (⁶⁰Co with 10K word limit)

#![allow(dead_code)]
use num_bigint::BigInt;
use num_traits::{Zero, One, Signed};
use rustc_hash::FxHashMap;
use std::collections::BTreeMap;
use rug::Float as MpFloat;
use rug::ops::Pow;
use std::time::Instant;

// ════════════════════════════════════════════════════════════════
// Laurent polynomial in t = q^{1/2} over ℤ (BigInt coefficients)
// ════════════════════════════════════════════════════════════════

#[derive(Clone, Debug, PartialEq, Eq, Default)]
struct LPoly { terms: BTreeMap<i32, BigInt> }

impl LPoly {
    fn zero() -> Self { Self { terms: BTreeMap::new() } }
    fn one() -> Self { let mut p = Self::zero(); p.terms.insert(0, BigInt::one()); p }
    fn t(power: i32) -> Self { let mut p = Self::zero(); p.terms.insert(power, BigInt::one()); p }
    fn is_zero(&self) -> bool { self.terms.is_empty() }
    fn n_terms(&self) -> usize { self.terms.len() }

    fn add(&self, other: &LPoly) -> LPoly {
        let mut r = self.clone();
        for (k, v) in &other.terms {
            let e = r.terms.entry(*k).or_insert_with(BigInt::zero);
            *e += v;
            if e.is_zero() { r.terms.remove(k); }
        }
        r
    }
    fn scale(&self, s: &BigInt) -> LPoly {
        if s.is_zero() { return Self::zero(); }
        let mut r = BTreeMap::new();
        for (k, v) in &self.terms {
            let val = v * s;
            if !val.is_zero() { r.insert(*k, val); }
        }
        LPoly { terms: r }
    }
    fn scale_i64(&self, s: i64) -> LPoly {
        self.scale(&BigInt::from(s))
    }
    fn mul(&self, other: &LPoly) -> LPoly {
        let mut r: BTreeMap<i32, BigInt> = BTreeMap::new();
        for (k1, v1) in &self.terms {
            for (k2, v2) in &other.terms {
                let k = k1 + k2;
                let val = v1 * v2;
                let e = r.entry(k).or_insert_with(BigInt::zero);
                *e += val;
                if e.is_zero() { r.remove(&k); }
            }
        }
        LPoly { terms: r }
    }
    fn shift(&self, n: i32) -> LPoly {
        let mut r = BTreeMap::new();
        for (k, v) in &self.terms { r.insert(k + n, v.clone()); }
        LPoly { terms: r }
    }
    fn eval_f64(&self, t: f64) -> f64 {
        self.terms.iter().map(|(k, v)| {
            let c: f64 = v.to_string().parse().unwrap_or(0.0);
            c * t.powi(*k)
        }).sum()
    }

    /// Evaluate F_Pauli = |num/den| at t using full BigInt rational arithmetic.
    ///
    /// Approximates t as a high-precision rational p_t/q_t, then evaluates
    /// both polynomials exactly as BigInt rationals. No f64 precision loss.
    fn eval_ratio_f64(num: &LPoly, den: &LPoly, t: f64) -> f64 {
        if den.is_zero() { return f64::NAN; }
        if num.is_zero() { return 0.0; }

        // Approximate t = sqrt(q₀) as rational with 30-digit precision.
        // t ≈ 1053556078... / 10^18
        // Use 18-digit approximation: enough for ~15 digits of F_Pauli.
        let scale = 1_000_000_000_000_000_000i128; // 10^18
        let t_approx = (t * scale as f64).round() as i128;
        let p_t = BigInt::from(t_approx);
        let q_t = BigInt::from(scale);

        // Evaluate poly at p_t/q_t:
        // poly(p_t/q_t) = Σ c_k × (p_t/q_t)^k
        // = (1/q_t^max_pow) × Σ c_k × p_t^k × q_t^(max_pow - k)
        fn eval_rational(poly: &LPoly, p_t: &BigInt, q_t: &BigInt) -> (BigInt, BigInt) {
            if poly.terms.is_empty() { return (BigInt::zero(), BigInt::one()); }
            let min_exp = *poly.terms.keys().min().unwrap();
            let max_exp = *poly.terms.keys().max().unwrap();

            // poly(p/q) = Σ c_k × (p/q)^k
            // Common denominator: p^|min_exp| × q^max_exp
            // Numerator term k: c_k × p^(k + |min_exp|) × q^(max_exp - k)
            let neg_min = if min_exp < 0 { (-min_exp) as usize } else { 0 };
            let pos_max = if max_exp > 0 { max_exp as usize } else { 0 };

            // Max power of p needed: max_exp + neg_min
            // Max power of q needed: pos_max + neg_min (for most negative k)
            let max_p_pow = (max_exp - min_exp) as usize;  // = max_exp + |min_exp|
            let max_q_pow = (max_exp - min_exp) as usize;  // same span

            let mut p_pows: Vec<BigInt> = vec![BigInt::one()];
            let mut q_pows: Vec<BigInt> = vec![BigInt::one()];
            for _ in 0..max_p_pow {
                p_pows.push(p_pows.last().unwrap() * p_t);
            }
            for _ in 0..max_q_pow {
                q_pows.push(q_pows.last().unwrap() * q_t);
            }

            let mut numer = BigInt::zero();
            for (&k, coeff) in &poly.terms {
                // p power: k - min_exp (always >= 0)
                let p_idx = (k - min_exp) as usize;
                // q power: max_exp - k (always >= 0)
                let q_idx = (max_exp - k) as usize;
                let term = coeff * &p_pows[p_idx] * &q_pows[q_idx];
                numer += term;
            }

            // Denominator = p^neg_min × q^pos_max
            // These indices are within the precomputed range since
            // neg_min + pos_max ≤ max_exp - min_exp = max_p_pow
            let p_den = if neg_min < p_pows.len() { p_pows[neg_min].clone() } else {
                let mut r = BigInt::one();
                for _ in 0..neg_min { r *= p_t; }
                r
            };
            let q_den = if pos_max < q_pows.len() { q_pows[pos_max].clone() } else {
                let mut r = BigInt::one();
                for _ in 0..pos_max { r *= q_t; }
                r
            };
            let denom = p_den * q_den;
            (numer, denom)
        }

        let (n_num, n_den) = eval_rational(num, &p_t, &q_t);
        let (d_num, d_den) = eval_rational(den, &p_t, &q_t);

        // F = |n_num/n_den| / |d_num/d_den| = |n_num × d_den| / |n_den × d_num|
        let final_num = (&n_num * &d_den).abs();
        let final_den = (&n_den * &d_num).abs();

        if final_den.is_zero() { return f64::NAN; }

        // Convert BigInt ratio to f64
        Self::bigint_ratio_f64(&final_num, &final_den)
    }

    /// Convert BigInt ratio a/b to f64.
    fn bigint_ratio_f64(a: &BigInt, b: &BigInt) -> f64 {
        if b.is_zero() { return f64::NAN; }
        let a_str = a.to_string();
        let b_str = b.to_string();
        // Use leading 15 digits + digit count difference
        let a_len = a_str.len();
        let b_len = b_str.len();
        let a_lead: f64 = a_str[..std::cmp::min(15, a_len)].parse().unwrap_or(0.0);
        let b_lead: f64 = b_str[..std::cmp::min(15, b_len)].parse().unwrap_or(1.0);
        let exp_diff = (a_len as i32 - std::cmp::min(15, a_len) as i32)
                     - (b_len as i32 - std::cmp::min(15, b_len) as i32);
        (a_lead / b_lead) * 10.0_f64.powi(exp_diff)
    }
    /// 2-adic valuation of a BigInt: largest k such that 2^k | n.
    fn v2(n: &BigInt) -> u32 {
        if n.is_zero() { return u32::MAX; }
        let (_, bytes) = n.to_bytes_le();
        let mut v = 0u32;
        for &b in &bytes {
            if b == 0 { v += 8; }
            else { v += b.trailing_zeros(); break; }
        }
        v
    }

    /// Minimum 2-adic valuation across all coefficients.
    fn min_v2(&self) -> u32 {
        self.terms.values()
            .filter(|v| !v.is_zero())
            .map(|v| Self::v2(v))
            .min()
            .unwrap_or(0)
    }

    /// Divide all coefficients by 2^k (exact division).
    fn shift_v2(&self, k: u32) -> LPoly {
        if k == 0 { return self.clone(); }
        let divisor = BigInt::from(1) << k;
        let mut r = BTreeMap::new();
        for (exp, v) in &self.terms {
            if v.is_zero() { continue; }
            r.insert(*exp, v / &divisor);
        }
        LPoly { terms: r }
    }

    /// Evaluate polynomial at t using mpfr with `prec` bits of precision.
    /// Returns the result as an MpFloat.
    fn eval_mpfr(&self, t_f64: f64, prec: u32) -> MpFloat {
        let t = MpFloat::with_val(prec, t_f64);
        let mut sum = MpFloat::with_val(prec, 0.0);

        // Precompute powers of t for positive and negative exponents
        let min_exp = self.terms.keys().min().copied().unwrap_or(0);
        let max_exp = self.terms.keys().max().copied().unwrap_or(0);

        // t^k for each exponent
        for (&k, v) in &self.terms {
            if v.is_zero() { continue; }
            // Convert BigInt coefficient to MpFloat
            let c = MpFloat::with_val(prec, MpFloat::parse(v.to_string()).unwrap());
            // Compute t^k
            let tk = if k >= 0 {
                MpFloat::with_val(prec, t.clone().pow(k as u32))
            } else {
                let inv_t = MpFloat::with_val(prec, 1.0) / &t;
                MpFloat::with_val(prec, inv_t.pow((-k) as u32))
            };
            sum += c * tk;
        }
        sum
    }

    /// Evaluate |self/other| at t using mpfr. No f64 overflow.
    fn eval_ratio_mpfr(num: &LPoly, den: &LPoly, t_f64: f64, prec: u32) -> f64 {
        let n = num.eval_mpfr(t_f64, prec);
        let d = den.eval_mpfr(t_f64, prec);
        if d.is_zero() { return f64::NAN; }
        let ratio = MpFloat::with_val(prec, &n / &d);
        ratio.to_f64().abs()
    }

    fn max_abs_coeff_log10(&self) -> f64 {
        self.terms.values()
            .map(|v| {
                let s = v.abs().to_string();
                s.len() as f64 - 1.0 + (s.chars().next().unwrap().to_digit(10).unwrap_or(1) as f64).log10()
            })
            .fold(0.0f64, f64::max)
    }
    fn mem_bytes(&self) -> usize {
        self.terms.iter().map(|(_, v)| {
            32 + v.to_bytes_le().1.len()  // overhead + digit bytes
        }).sum()
    }
}

// ════════════════════════════════════════════════════════════════
// Packed word (reuse from v8 — same TreeWord structure)
// ════════════════════════════════════════════════════════════════

#[derive(Clone, Copy, PartialEq, Eq, Hash)]
struct W { data: [u128; 4], len: u8 }

impl W {
    const E: W = W { data: [0; 4], len: 0 };
    fn len(self) -> usize { self.len as usize }
    fn get(self, i: usize) -> u8 { ((self.data[i/16] >> ((i%16)*8)) & 0xFF) as u8 }
    fn set(&mut self, i: usize, v: u8) {
        let s = (i%16)*8; let w = i/16;
        self.data[w] = (self.data[w] & !(0xFF << s)) | ((v as u128) << s);
    }
    fn push(mut self, v: u8) -> W {
        let l = self.len as usize;
        if l >= 64 { return self; }
        let s = (l%16)*8; let w = l/16;
        self.data[w] |= (v as u128) << s;
        self.len += 1;
        self
    }
    fn remove_at(self, pos: usize) -> W {
        let l = self.len();
        let mut r = W::E;
        let mut j = 0;
        for i in 0..l { if i != pos { r = r.push(self.get(i)); j += 1; } }
        r
    }
    fn drop_last(self) -> W {
        if self.len == 0 { return self; }
        let mut r = W::E;
        for i in 0..self.len() - 1 { r = r.push(self.get(i)); }
        r
    }

    fn junction_check(self) -> Option<(usize, u8)> {
        let l = self.len();
        if l < 2 { return None; }
        let p = l-2;
        let a = self.get(p); let b = self.get(p+1);
        if a == b { return Some((p, 0)); }
        if (a as i16 - b as i16) >= 2 { return Some((p, 1)); }
        if l >= 3 {
            let c = self.get(l-3);
            if c == b && (c as i16 - a as i16).abs() == 1 && a < c {
                return Some((l-3, 2));
            }
        }
        None
    }
    fn find_reduction(self) -> Option<(usize, u8)> {
        let l = self.len();
        if l < 2 { return None; }
        for p in 0..l-1 {
            let a = self.get(p); let b = self.get(p+1);
            if a == b { return Some((p, 0)); }
            if (a as i16 - b as i16) >= 2 { return Some((p, 1)); }
            if p+2 < l {
                let c = self.get(p+2);
                if a == c && (a as i16 - b as i16).abs() == 1 && b < a { return Some((p, 2)); }
            }
        }
        None
    }
}

impl std::fmt::Debug for W {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        let l = self.len();
        if l == 0 { return write!(f, "𝟏"); }
        for i in 0..l { if i > 0 { write!(f, ".")?; } write!(f, "σ{}", self.get(i))?; }
        Ok(())
    }
}

// ════════════════════════════════════════════════════════════════
// Symbolic Hecke element (BigInt version)
// ════════════════════════════════════════════════════════════════

struct Elem { terms: FxHashMap<W, LPoly>, pn_count: u32 }

impl Elem {
    fn identity() -> Self {
        let mut h = Self { terms: FxHashMap::default(), pn_count: 0 };
        h.terms.insert(W::E, LPoly::one());
        h
    }
    fn n_terms(&self) -> usize { self.terms.len() }
    fn total_poly_terms(&self) -> usize { self.terms.values().map(|c| c.n_terms()).sum() }
    fn mem_bytes(&self) -> usize { self.terms.iter().map(|(_, c)| 72 + c.mem_bytes()).sum() }
    fn max_coeff_log10(&self) -> f64 {
        self.terms.values().map(|c| c.max_abs_coeff_log10()).fold(0.0f64, f64::max)
    }
}

// ════════════════════════════════════════════════════════════════
// Crossing coefficients and engine
// ════════════════════════════════════════════════════════════════

fn ha_poly() -> LPoly {
    let mut p = LPoly::zero();
    p.terms.insert(2, BigInt::one());
    p.terms.insert(-2, -BigInt::one());
    p
}

/// Crossing coefficients (c, d) in ℤ[t, t⁻¹] where t = q^½ (BigInt).
///
/// From the Hecke inverse relation σ⁻¹ = σ − (q − q⁻¹):
///   pp → σ:          c = 1,   d = 0
///   nn → σ⁻¹:        c = 1,   d = −HA = −(t² − t⁻²) = −t² + t⁻²
///   pn → ½(σ+σ⁻¹): c = 1,   d = −HA/2
///        (doubled to stay integral: 2c = 2, 2d = −t² + t⁻²)
fn crossing_sym(ti: u8, tj: u8) -> (LPoly, LPoly, bool) {
    match (ti, tj) {
        (b'p', b'p') => (LPoly::one(), LPoly::zero(), false),
        (b'n', b'n') => {
            // c = 1, d = −HA = −t² + t⁻²
            let c = LPoly::one();
            let mut d = LPoly::zero();
            d.terms.insert(2, -BigInt::one());   // −t²
            d.terms.insert(-2, BigInt::one());   // +t⁻²
            (c, d, false)
        }
        _ => {
            // pn: doubled to stay integral.
            // 2c = 2, 2d = −HA = −t² + t⁻²
            let mut c2 = LPoly::zero();
            c2.terms.insert(0, BigInt::from(2));   // 2
            let mut d2 = LPoly::zero();
            d2.terms.insert(2, -BigInt::one());    // −t²
            d2.terms.insert(-2, BigInt::one());    // +t⁻²
            (c2, d2, true)
        }
    }
}

// ════════════════════════════════════════════════════════════════
// Pauli accumulator (BigInt version)
// ════════════════════════════════════════════════════════════════

#[derive(Clone)]
struct SymPauliAcc {
    tr_alt: LPoly,
    net: LPoly,
    net_by_len: Vec<LPoly>,
}

impl SymPauliAcc {
    fn zero() -> Self { Self { tr_alt: LPoly::zero(), net: LPoly::zero(), net_by_len: Vec::new() } }

    fn add_term(&mut self, coeff: &LPoly, word_len: usize) {
        self.net = self.net.add(coeff);
        let l = word_len as i64;
        let sign = if l % 2 == 0 { 1i64 } else { -1i64 };
        self.tr_alt = self.tr_alt.add(&coeff.scale_i64(sign).shift(-2 * word_len as i32));
        // Per-length tracking
        while self.net_by_len.len() <= word_len {
            self.net_by_len.push(LPoly::zero());
        }
        self.net_by_len[word_len] = self.net_by_len[word_len].add(coeff);
    }

    fn merge(&mut self, other: &SymPauliAcc) {
        self.tr_alt = self.tr_alt.add(&other.tr_alt);
        self.net = self.net.add(&other.net);
        for (i, p) in other.net_by_len.iter().enumerate() {
            while self.net_by_len.len() <= i {
                self.net_by_len.push(LPoly::zero());
            }
            self.net_by_len[i] = self.net_by_len[i].add(p);
        }
    }

    fn add_from_elem(&mut self, elem: &Elem) {
        for (w, c) in &elem.terms {
            self.add_term(c, w.len());
        }
    }
}

// ════════════════════════════════════════════════════════════════
// Engine core
// ════════════════════════════════════════════════════════════════

struct Eng;

impl Eng {
    fn multiply_and_reduce(elem: &mut Elem, gen: u8, c: &LPoly, d: &LPoly, is_dbl: bool, ha: &LPoly) {
        if is_dbl { elem.pn_count += 1; }
        let old: Vec<(W, LPoly)> = elem.terms.drain().collect();
        let mut stable: FxHashMap<W, LPoly> = FxHashMap::default();
        let mut pending: Vec<(W, LPoly)> = Vec::new();

        for (w, coeff) in old {
            if !d.is_zero() {
                let e = stable.entry(w).or_insert(LPoly::zero());
                *e = e.add(&coeff.mul(d));
            }
            if !c.is_zero() {
                pending.push((w.push(gen), coeff.mul(c)));
            }
        }

        loop {
            let mut next: Vec<(W, LPoly)> = Vec::new();
            let mut any_reduced = false;
            for (word, coeff) in pending {
                if coeff.is_zero() { continue; }
                let red = word.junction_check().or_else(|| word.find_reduction());
                if let Some((pos, rule)) = red {
                    any_reduced = true;
                    match rule {
                        0 => {
                            let w1 = word.remove_at(pos + 1);
                            let w2 = w1.remove_at(pos);
                            next.push((w1, coeff.mul(ha)));
                            next.push((w2, coeff));
                        }
                        1 => {
                            let mut w = word;
                            let (a, b) = (w.get(pos), w.get(pos + 1));
                            w.set(pos, b); w.set(pos + 1, a);
                            next.push((w, coeff));
                        }
                        2 => {
                            let mut w = word;
                            let (a, b) = (w.get(pos), w.get(pos + 1));
                            w.set(pos, b); w.set(pos + 1, a); w.set(pos + 2, b);
                            next.push((w, coeff));
                        }
                        _ => {}
                    }
                } else {
                    let e = stable.entry(word).or_insert(LPoly::zero());
                    *e = e.add(&coeff);
                }
            }
            if !any_reduced { break; }
            let mut consolidated: FxHashMap<W, LPoly> = FxHashMap::default();
            for (w, c) in next {
                if c.is_zero() { continue; }
                let e = consolidated.entry(w).or_insert(LPoly::zero());
                *e = e.add(&c);
            }
            pending = Vec::new();
            for (w, c) in consolidated {
                if c.is_zero() { continue; }
                if let Some(existing) = stable.remove(&w) {
                    let merged = existing.add(&c);
                    if !merged.is_zero() && w.find_reduction().is_some() {
                        pending.push((w, merged));
                    } else if !merged.is_zero() {
                        stable.insert(w, merged);
                    }
                } else {
                    pending.push((w, c));
                }
            }
        }
        stable.retain(|_, c| !c.is_zero());
        elem.terms = stable;

        // Inline GCD reduction: keep BigInt sizes bounded
        let gv = elem.terms.values()
            .filter(|c| !c.is_zero())
            .map(|c| c.min_v2())
            .min().unwrap_or(0);
        if gv > 0 {
            for c in elem.terms.values_mut() {
                *c = c.shift_v2(gv);
            }
        }
    }

    fn strip_with_pauli(terms: &mut FxHashMap<W, LPoly>) -> SymPauliAcc {
        let mut removed = SymPauliAcc::zero();
        // Iterate I9+I8 until convergence (not just single pass)
        loop {
            let mut any_removed = false;
            // I9: strip words whose prefix is present (longest first)
            let max_len = terms.keys().map(|w| w.len()).max().unwrap_or(0);
            for tl in (2..=max_len).rev() {
                let to_rm: Vec<W> = terms.keys()
                    .filter(|w| w.len() == tl && !terms[*w].is_zero())
                    .filter(|w| terms.get(&w.drop_last()).map_or(false, |c| !c.is_zero()))
                    .cloned().collect();
                for w in &to_rm {
                    if let Some(c) = terms.remove(w) {
                        removed.add_term(&c, w.len());
                        any_removed = true;
                    }
                }
            }
            // I8: strip adjacent pairs [i, i+1] where [i+1] is present
            let adj: Vec<W> = terms.keys()
                .filter(|w| w.len() == 2 && !terms[*w].is_zero() && w.get(1) == w.get(0) + 1)
                .filter(|w| terms.get(&W::E.push(w.get(1))).map_or(false, |c| !c.is_zero()))
                .cloned().collect();
            for w in &adj {
                if let Some(c) = terms.remove(w) {
                    removed.add_term(&c, w.len());
                    any_removed = true;
                }
            }
            if !any_removed { break; }
        }
        terms.retain(|_, c| !c.is_zero());
        removed
    }

    fn build(z: usize, n: usize, mid_threshold: usize) -> (Elem, SymPauliAcc) {
        let a = z + n;
        let ha = ha_poly();
        let mut types = vec![b'p'; z];
        types.extend(vec![b'n'; n]);
        let mut elem = Elem::identity();
        let mut accum = SymPauliAcc::zero();
        let t0 = Instant::now();
        // For A ≤ 12: NO mid-construction stripping — build full raw NF,
        // then strip once at the end. This gives the correct A-term basis.
        // For A > 12: eager stripping keeps memory bounded, but the final
        // strip may leave extra words (orphaned by early prefix removal).
        let no_mid_strip = a <= 12;
        let strip_after = if no_mid_strip { 999 } else { 2 };  // strip from strand 2 onwards for A > 10
        let mut total_mid_strips: u64 = 0;
        let eager = !no_mid_strip && mid_threshold == 0;
        let effective_threshold = if eager { usize::MAX } else { mid_threshold };

        for k in 1..a {
            for i in 0..k {
                let tc = Instant::now();
                let n_before = elem.n_terms();
                let (c, d, dbl) = crossing_sym(types[i], types[k]);
                Self::multiply_and_reduce(&mut elem, i as u8, &c, &d, dbl, &ha);

                // Strip condition: eager (always) or threshold exceeded
                // Strip aggressively for large A: after EVERY crossing when A > 16
                let should_strip = (a > 16)
                    || (eager && k >= strip_after)
                    || elem.n_terms() > effective_threshold;

                if should_strip {
                    let n_pre = elem.n_terms();
                    let removed = Self::strip_with_pauli(&mut elem.terms);
                    accum.merge(&removed);
                    total_mid_strips += 1;
                    // GCD reduction: divide out common power of 2 from ALL LPoly coefficients
                    // Each elem.terms[w] is a LPoly. Find min v2 across all BigInt coeffs
                    // in all LPolys, then shift all of them.
                    let global_min_v2 = elem.terms.values()
                        .filter(|lp| !lp.is_zero())
                        .map(|lp| lp.min_v2())
                        .min().unwrap_or(0);
                    if global_min_v2 > 0 {
                        for lp in elem.terms.values_mut() {
                            *lp = lp.shift_v2(global_min_v2);
                        }
                    }
                    let ms = tc.elapsed().as_millis();
                    if ms > 50 || n_pre > 1000 {
                        eprintln!("    ({},{}) {}-{}: {} → {} → {} words (strip), {}ms",
                            i, k, types[i] as char, types[k] as char,
                            n_before, n_pre, elem.n_terms(), ms);
                    }
                } else {
                    let ms = tc.elapsed().as_millis();
                    if ms > 100 || elem.n_terms() > 5000 {
                        eprintln!("    ({},{}) {}-{}: {} → {} words, {}ms",
                            i, k, types[i] as char, types[k] as char,
                            n_before, elem.n_terms(), ms);
                    }
                }
            }

            let mc = elem.max_coeff_log10();
            let mb = elem.mem_bytes() as f64 / 1_048_576.0;
            let elapsed = t0.elapsed().as_secs_f64();

            // Always strip at strand boundary for A > 9
            if (k + 1) > strip_after {
                let n_pre = elem.n_terms();
                let removed = Self::strip_with_pauli(&mut elem.terms);
                accum.merge(&removed);
                // GCD reduction at strand boundary
                let global_min_v2 = elem.terms.values()
                    .filter(|lp| !lp.is_zero())
                    .map(|lp| lp.min_v2())
                    .min().unwrap_or(0);
                if global_min_v2 > 0 {
                    for lp in elem.terms.values_mut() {
                        *lp = lp.shift_v2(global_min_v2);
                    }
                }
                let mc2 = elem.max_coeff_log10();
                eprintln!("  strand {}/{}: {} → {} words, coeff~10^{:.0}→{:.0}, {:.0}MB, {:.1}s [{}s]",
                    k, a - 1, n_pre, elem.n_terms(), mc, mc2, mb, elapsed, total_mid_strips);
            } else {
                eprintln!("  strand {}/{}: {} words, coeff~10^{:.0}, {:.0}MB, {:.1}s",
                    k, a - 1, elem.n_terms(), mc, mb, elapsed);
            }
        }
        (elem, accum)
    }
}

// ════════════════════════════════════════════════════════════════
// Exact Ocneanu (Markov) trace, convention D
// ════════════════════════════════════════════════════════════════
//
// The element is re-expanded in the T_w (permutation) basis of H_A(q), where
// T_w T_s = T_{ws} if ws > w, and T_{ws} + h T_w otherwise (σ² = hσ + 1,
// h = t² − t⁻²). The trace is the unique one with tr(x T_{n−1} y) = z·tr(xy),
// computed by peeling the strand n−1 off each permutation; it is a polynomial
// in z with Laurent-polynomial coefficients in t, and only then is
// z = q³/(q²+1) substituted. Ported from
// computations/probes/v9_markov_trace_convention_d_probe.py, which checks the
// same recursion for cyclicity and the Markov property. Bean qou-m7py.

const Q0_50: &str = "1.1099785827513808075916690956107688798744991218736";
const TW_CAP: usize = 4_000_000;

mod markov {
    use super::{LPoly, Elem, MpFloat, Pow};
    use num_bigint::BigInt;
    use num_traits::{One, Zero};
    use rustc_hash::FxHashMap;

    /// z-polynomial: entry k is the coefficient of z^k.
    pub type ZPoly = Vec<LPoly>;
    type Tw = FxHashMap<Vec<u8>, LPoly>;

    fn h() -> LPoly {
        let mut p = LPoly::zero();
        p.terms.insert(2, BigInt::one());
        p.terms.insert(-2, -BigInt::one());
        p
    }

    fn add_into(m: &mut Tw, k: Vec<u8>, v: LPoly) {
        let e = m.entry(k).or_insert_with(LPoly::zero);
        *e = e.add(&v);
    }

    /// e · T_{s_i}
    fn mul_s(e: &Tw, i: usize, h: &LPoly) -> Tw {
        let mut out: Tw = FxHashMap::default();
        for (w, c) in e {
            let mut ws = w.clone();
            ws.swap(i, i + 1);
            add_into(&mut out, ws, c.clone());
            if w[i] > w[i + 1] {
                add_into(&mut out, w.clone(), c.mul(h));
            }
        }
        out.retain(|_, c| !c.is_zero());
        out
    }

    fn zp_add_scaled(acc: &mut ZPoly, c: &LPoly, p: &ZPoly, shift: usize) {
        for (k, pk) in p.iter().enumerate() {
            if pk.is_zero() { continue; }
            while acc.len() <= k + shift { acc.push(LPoly::zero()); }
            acc[k + shift] = acc[k + shift].add(&c.mul(pk));
        }
    }

    struct Tracer { memo: FxHashMap<Vec<u8>, ZPoly>, h: LPoly }

    impl Tracer {
        fn new() -> Self { Self { memo: FxHashMap::default(), h: h() } }

        fn tr_perm(&mut self, w: &[u8]) -> ZPoly {
            if let Some(r) = self.memo.get(w) { return r.clone(); }
            let n = w.len();
            let r = if n == 0 {
                vec![LPoly::one()]
            } else if w[n - 1] as usize == n - 1 {
                self.tr_perm(&w[..n - 1])
            } else {
                // w = x · s_{n−2} ⋯ s_j with x ∈ S_{n−1}; Markov removes s_{n−2}.
                let j = w.iter().position(|&v| v as usize == n - 1).unwrap();
                let mut x = w.to_vec();
                x.remove(j);
                let mut e: Tw = FxHashMap::default();
                e.insert(x, LPoly::one());
                if n >= 3 {
                    let mut i = n - 3;
                    while i >= j {
                        e = mul_s(&e, i, &self.h);
                        if i == 0 { break; }
                        i -= 1;
                    }
                }
                let mut acc: ZPoly = Vec::new();
                for (u, c) in &e {
                    let tu = self.tr_perm(u);
                    zp_add_scaled(&mut acc, c, &tu, 1);
                }
                acc
            };
            self.memo.insert(w.to_vec(), r.clone());
            r
        }

        fn trace(&mut self, e: &Tw) -> ZPoly {
            let mut acc: ZPoly = Vec::new();
            for (w, c) in e {
                let tw = self.tr_perm(w);
                zp_add_scaled(&mut acc, c, &tw, 0);
            }
            acc
        }
    }

    fn word_tw(word: &[usize], a: usize, coeff: &LPoly, h: &LPoly, cap: usize) -> Option<Tw> {
        let mut e: Tw = FxHashMap::default();
        e.insert((0..a as u8).collect(), coeff.clone());
        for &g in word {
            e = mul_s(&e, g, h);
            if e.len() > cap { return None; }
        }
        Some(e)
    }

    /// tr(σ₀σ₁σ₀) = h·z² + z: the identity gram.rs TR_M[5] records.
    fn self_check() {
        let h = h();
        let e = word_tw(&[0, 1, 0], 3, &LPoly::one(), &h, 100).unwrap();
        let tr = Tracer::new().trace(&e);
        let want: ZPoly = vec![LPoly::zero(), LPoly::one(), h];
        let trim = |p: &ZPoly| -> Vec<LPoly> {
            let mut v = p.clone();
            while v.last().map_or(false, |x| x.is_zero()) { v.pop(); }
            v
        };
        assert_eq!(trim(&tr), trim(&want), "Markov trace self-check failed");
    }

    /// Exact trace of the normal-form element, or None if a word's T_w
    /// expansion exceeds `cap` permutations.
    pub fn trace_of_elem(elem: &Elem, a: usize, cap: usize) -> Option<ZPoly> {
        self_check();
        let h = h();
        let mut total: Tw = FxHashMap::default();
        for (w, c) in &elem.terms {
            let word: Vec<usize> = (0..w.len()).map(|i| w.get(i) as usize).collect();
            for (k, v) in word_tw(&word, a, c, &h, cap)? {
                add_into(&mut total, k, v);
            }
            if total.len() > cap { return None; }
        }
        total.retain(|_, c| !c.is_zero());
        Some(Tracer::new().trace(&total))
    }

    pub fn exact_terms(tr: &ZPoly) -> Vec<(usize, i32, String)> {
        let mut out = Vec::new();
        for (k, p) in tr.iter().enumerate() {
            for (e, v) in &p.terms {
                if !v.is_zero() { out.push((k, *e, v.to_string())); }
            }
        }
        out
    }

    /// Σ_k tr_k(t) z^k at q₀ (50-digit proton pin), z = q³/(q²+1), ÷ 2^pn,
    /// as a 60-significant-digit decimal string.
    pub fn eval_conv_d(tr: &ZPoly, pn: u32) -> String {
        let maxc = tr.iter().flat_map(|p| p.terms.values())
            .map(|v| v.to_string().len()).max().unwrap_or(1) as u32;
        let prec = 4 * (maxc + 200);
        let q = MpFloat::with_val(prec, MpFloat::parse(super::Q0_50).unwrap());
        let t = MpFloat::with_val(prec, q.sqrt_ref());
        let q2 = MpFloat::with_val(prec, &q * &q);
        let z = MpFloat::with_val(prec, MpFloat::with_val(prec, &q2 * &q) / (q2 + 1u32));
        let tinv = MpFloat::with_val(prec, 1u32) / &t;
        let mut sum = MpFloat::with_val(prec, 0u32);
        let mut zk = MpFloat::with_val(prec, 1u32);
        for p in tr {
            for (e, v) in &p.terms {
                let c = MpFloat::with_val(prec, MpFloat::parse(v.to_string()).unwrap());
                let te = if *e >= 0 {
                    MpFloat::with_val(prec, t.clone().pow(*e as u32))
                } else {
                    MpFloat::with_val(prec, tinv.clone().pow((-*e) as u32))
                };
                sum += MpFloat::with_val(prec, &c * &te) * &zk;
            }
            zk = MpFloat::with_val(prec, &zk * &z);
        }
        let den = MpFloat::with_val(prec, MpFloat::with_val(prec, 2u32).pow(pn));
        let v = MpFloat::with_val(prec, sum / den);
        v.to_string_radix(10, Some(60))
    }
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.len() < 3 {
        eprintln!("hecke-bigint (v9) — BigInt symbolic Pauli witness, exact in q");
        eprintln!("Usage: hecke-bigint Z N [mid_strip_threshold]");
        eprintln!("  Z N: nucleus (e.g. 27 33 for ⁶⁰Co)");
        eprintln!("  mid_strip_threshold: 0 = eager (strip after EVERY crossing)");
        eprintln!("                       N = strip when words > N (default: 50000)");
        eprintln!("  Eager mode recommended for A > 20.");
        std::process::exit(1);
    }

    let z: usize = args[1].parse().unwrap();
    let n: usize = args[2].parse().unwrap();
    let mid_threshold: usize = args.get(3).and_then(|s| s.parse().ok())
        .unwrap_or(if z + n > 20 { 0 } else { 50000 });
    let a = z + n;

    eprintln!("hecke-bigint v9 — BigInt symbolic engine");
    eprintln!("  A={} (Z={}, N={}), mid-strip: {}",
        a, z, n, if mid_threshold == 0 { "EAGER (every crossing)".to_string() }
                 else { format!("threshold {}", mid_threshold) });
    eprintln!("  No i128 overflow — arbitrary precision coefficients");

    let t0 = Instant::now();
    let (mut elem, accum) = Eng::build(z, n, mid_threshold);

    // Final full strip: the mid-construction strip can't remove all words
    // because prefixes created by later crossings weren't present yet.
    // Now that construction is complete, iterate I9+I8 to convergence.
    let pre_final = elem.n_terms();

    // Optional per-word dump of the complete normal-form element, BEFORE the
    // final strip. Only the full crossing product when `accum` is empty, i.e.
    // nothing was stripped mid-construction. Bean qou-m7py.
    if let Ok(path) = std::env::var("V9_DUMP_ELEM") {
        let mut words: Vec<(Vec<u8>, Vec<(i32, String)>)> = elem.terms.iter()
            .map(|(w, c)| ((0..w.len()).map(|i| w.get(i)).collect(),
                           c.terms.iter().map(|(k, v)| (*k, v.to_string())).collect()))
            .collect();
        words.sort();
        let mid_stripped = !accum.net.is_zero() || !accum.net_by_len.is_empty();
        let dump = serde_json::json!({
            "z": z, "n": n, "a": a, "pn_count": elem.pn_count,
            "variable": "t = q^(1/2); word letters are 0-based generators",
            "mid_construction_strip": mid_stripped,
            "words": words,
        });
        std::fs::write(&path, serde_json::to_string(&dump).unwrap()).unwrap();
        eprintln!("  dumped {} words to {} (mid-strip: {})", elem.n_terms(), path, mid_stripped);
    }

    // Exact Ocneanu trace at convention D, z = q³/(q²+1), of the full
    // crossing product. Taken here, before the final Pauli strip, and only
    // when nothing was stripped mid-construction: a stripped element is not
    // the product, so its trace would not be the nucleus's.
    let tr_markov_d = {
        use hecke_engine::certificate::MarkovTraceD;
        let mid_stripped = !accum.net.is_zero() || !accum.net_by_len.is_empty();
        let base = |computed: bool| MarkovTraceD {
            computed, value: None, exact_z_t: None, reason: None,
            z: "q^3/(q^2+1)".to_string(),
            q0: Q0_50.to_string(),
            normalisation: "divided by 2^pn_count, like the *_f64 fields".to_string(),
        };
        if mid_stripped {
            let mut r = base(false);
            r.reason = Some("element was stripped mid-construction, so it is not the \
                crossing product and its trace is not defined here".to_string());
            r
        } else {
            match markov::trace_of_elem(&elem, a, TW_CAP) {
                Some(tr) => {
                    let mut r = base(true);
                    r.value = Some(markov::eval_conv_d(&tr, elem.pn_count));
                    r.exact_z_t = Some(markov::exact_terms(&tr));
                    eprintln!("  tr_M^D(q₀)/2^pn = {}", r.value.as_ref().unwrap());
                    r
                }
                None => {
                    let mut r = base(false);
                    r.reason = Some(format!("T_w expansion exceeded {} permutations", TW_CAP));
                    r
                }
            }
        }
    };

    let final_removed = Eng::strip_with_pauli(&mut elem.terms);
    let post_final = elem.n_terms();

    // Accumulate: mid-construction stripped + final stripped + remaining survivors
    let mut total = accum.clone();
    total.merge(&final_removed);
    let mut kept = SymPauliAcc::zero();
    kept.add_from_elem(&elem);  // only survivors after final strip
    total.merge(&kept);
    if pre_final != post_final {
        eprintln!("\n  Final strip: {} → {} words ({} absorbed)",
            pre_final, post_final, pre_final - post_final);
    }

    let elapsed = t0.elapsed().as_secs_f64();
    let mc = elem.max_coeff_log10();

    eprintln!("\n  Result: {} words (expected {}), coeff~10^{:.0}, {:.0}MB, {:.1}s",
        elem.n_terms(), z + n, mc, elem.mem_bytes() as f64 / 1e6, elapsed);

    // Evaluate F_Pauli = |tr_alt/net| at q₀.
    //
    // 2-adic normalization: the pn_count denominator is 2^891 for ⁶⁰Co.
    // Many polynomial coefficients are divisible by large powers of 2.
    // Factor these out to reduce effective coefficient size.
    // Substrate anchor. WAS the 5-significant-digit literal `1.10998`, which
    // is 1277 ppb from the proton pin -- 111x the muon/proton gap the
    // 2026-08-15 re-pin was about, and it silently set the accuracy of every
    // `*_f64` field in the 35 certificates this binary produced. The exact
    // symbolic `tr_alt`/`net` polynomials are unaffected (they are exact in
    // q); only the evaluations at q0 were.
    let q0: f64 = hecke_engine::gram::Q_0;
    let t0_val = q0.sqrt();

    // 2-adic normalization: find common factors of 2
    let v2_alt = total.tr_alt.min_v2();
    let v2_net = total.net.min_v2();
    let pn = elem.pn_count;

    eprintln!("\n  2-adic analysis:");
    eprintln!("    pn_count (denominator 2^{})", pn);
    eprintln!("    v₂(tr_alt) = {} (all coeffs divisible by 2^{})", v2_alt, v2_alt);
    eprintln!("    v₂(net)    = {} (all coeffs divisible by 2^{})", v2_net, v2_net);

    // Normalize: divide out common 2-adic content
    let alt_norm = total.tr_alt.shift_v2(v2_alt);
    let net_norm = total.net.shift_v2(v2_net);
    let alt_denom_pow = pn - v2_alt;  // remaining denominator for tr_alt
    let net_denom_pow = pn - v2_net;  // remaining denominator for net

    eprintln!("    After normalization:");
    eprintln!("      tr_alt: coeff~10^{:.0}, denom 2^{}", alt_norm.max_abs_coeff_log10(), alt_denom_pow);
    eprintln!("      net:    coeff~10^{:.0}, denom 2^{}", net_norm.max_abs_coeff_log10(), net_denom_pow);

    // F_Pauli = |tr_alt/net| = |alt_norm / 2^alt_denom × 2^net_denom / net_norm|
    //         = |alt_norm / net_norm| × 2^(net_denom - alt_denom)
    let denom_diff = net_denom_pow as i64 - alt_denom_pow as i64;

    // Try f64 eval on normalized polynomials (much smaller coefficients)
    let alt_val = alt_norm.eval_f64(t0_val);
    let net_val_raw = net_norm.eval_f64(t0_val);

    let (f, tr_alt_val, net_val) = if alt_val.is_finite() && net_val_raw.is_finite() && net_val_raw.abs() > 1e-300 {
        let raw_ratio = (alt_val / net_val_raw).abs();
        let f = raw_ratio * 2.0_f64.powi(denom_diff as i32);
        let ta = alt_val / 2.0_f64.powi(alt_denom_pow as i32);
        let nv = net_val_raw / 2.0_f64.powi(net_denom_pow as i32);
        (f, ta, nv)
    } else {
        // f64 overflows — use mpfr with enough precision
        let prec = (mc as u32 + 100) * 4;  // ~4 bits per decimal digit + margin
        eprintln!("    Using mpfr with {} bits ({:.0} digits) precision", prec, prec as f64 * 0.301);
        let f = LPoly::eval_ratio_mpfr(&total.tr_alt, &total.net, t0_val, prec);
        // Also get actual values via mpfr
        let denom_mp = MpFloat::with_val(prec, 2.0).pow(elem.pn_count as u32);
        let ta_mp = total.tr_alt.eval_mpfr(t0_val, prec) / &denom_mp;
        let nv_mp = total.net.eval_mpfr(t0_val, prec) / &denom_mp;
        let ta = ta_mp.to_f64();
        let nv = nv_mp.to_f64();
        (f, ta, nv)
    };

    let sym = match z {
        1=>"H",2=>"He",3=>"Li",4=>"Be",5=>"B",6=>"C",7=>"N",8=>"O",
        9=>"F",10=>"Ne",11=>"Na",12=>"Mg",13=>"Al",14=>"Si",15=>"P",
        16=>"S",17=>"Cl",18=>"Ar",19=>"K",20=>"Ca",26=>"Fe",27=>"Co",
        28=>"Ni",38=>"Sr",55=>"Cs",82=>"Pb",83=>"Bi",_=>"?"
    };
    let par = match (z%2, n%2) { (0,0)=>"ee", (1,1)=>"oo", _=>"oA" };

    println!("F_Pauli({}{}) = {:.10} (exact in q, evaluated at q₀ = {})", a, sym, f, q0);
    println!("  tr_alt(q₀) = {:.10e}", tr_alt_val);
    println!("  net(q₀)    = {:.10e}", net_val);
    println!("  pn_count = {} (denom = 2^{})", elem.pn_count, elem.pn_count);
    println!("  max coeff ~10^{:.0}", mc);
    println!("  time = {:.1}s", elapsed);

    // Print jet bundle decomposition
    eprintln!("\n  Jet bundle (net by word length):");
    // The canonical proton anchor, not the 5-digit 1.10998 literal this used
    // to carry (1277 ppb off — the distance `classify_pin` calls
    // "truncated-5-digit"). Safe to change: this value reaches only the
    // stderr jet-bundle diagnostic below, never the emitted certificate, so
    // the committed certificates are unaffected.
    let q0_val: f64 = hecke_engine::gram::Q_0;
    let t0_f64 = q0_val.sqrt();
    let denom_f64 = 2.0_f64.powi(elem.pn_count as i32);
    for (k, jet) in total.net_by_len.iter().enumerate() {
        if jet.is_zero() { continue; }
        let val = jet.eval_f64(t0_f64);
        let n_terms = jet.terms.len();
        if denom_f64.is_finite() && denom_f64 > 0.0 {
            eprintln!("    J^{}: {} terms, net^({})≈{:+.6e} (÷2^{}={:+.6e})",
                k, n_terms, k, val, elem.pn_count, val / denom_f64);
        } else {
            eprintln!("    J^{}: {} terms, net^({})≈{:+.6e} (denom overflow)", k, n_terms, k, val);
        }
    }

    // Write certificate JSON
    use hecke_engine::certificate::*;
    let cert = WitnessCertificate {
        isotope: IsotopeInfo {
            z, n, a,
            symbol: sym.to_string(),
            name: format!("{}{}", a, sym),
            parity: par.to_string(),
        },
        engine: EngineInfo {
            name: "hecke-engine".to_string(),
            version: env!("CARGO_PKG_VERSION").to_string(),
            commit: option_env!("GIT_SHA").unwrap_or("unknown").to_string(),
            binary: "hecke-bigint (v9)".to_string(),
        },
        generation: Some(hecke_engine::provenance::Generation::capture(q0)),
        tr_alt: SparsePoly::from_btree(&total.tr_alt.terms),
        net: SparsePoly::from_btree(&total.net.terms),
        observable: {
            // J⁰ + J¹: identity + single generators
            let mut obs = LPoly::zero();
            if total.net_by_len.len() > 0 { obs = obs.add(&total.net_by_len[0]); }
            if total.net_by_len.len() > 1 { obs = obs.add(&total.net_by_len[1]); }
            SparsePoly::from_btree(&obs.terms)
        },
        color: {
            // J≥2: multi-body correlations
            let mut cor = LPoly::zero();
            for k in 2..total.net_by_len.len() {
                cor = cor.add(&total.net_by_len[k]);
            }
            SparsePoly::from_btree(&cor.terms)
        },
        jets: total.net_by_len.iter().map(|p| SparsePoly::from_btree(&p.terms)).collect(),
        pn_count: elem.pn_count,
        f_pauli_f64: if f.is_finite() { Some(f) } else { None },
        tr_alt_f64: if tr_alt_val.is_finite() { Some(tr_alt_val) } else { None },
        net_f64: if net_val.is_finite() { Some(net_val) } else { None },
        tr_markov_d,
        strands: Vec::new(), // TODO: collect during build
        total_words: elem.n_terms(),
        max_coeff_log10: mc,
        elapsed_seconds: elapsed,
        computed_at: String::new(), // TODO: chrono
    };

    let cert_path = format!("certificate-{}{}.json", a, sym.to_lowercase());
    match std::fs::write(&cert_path, serde_json::to_string_pretty(&cert).unwrap()) {
        Ok(_) => eprintln!("\n  Certificate written to {}", cert_path),
        Err(e) => eprintln!("\n  Failed to write certificate: {}", e),
    }
}
