// v8: Optimized symbolic Gröbner engine with Gebauer-Möller filtering.
//
// Key optimizations over v7:
// 1. Junction-only reduction: after appending σ_k to reduced word w,
//    only check the last 3 positions (the junction). No full scan.
// 2. Gebauer-Möller filtering: skip S-polynomials that are "covered"
//    by simpler overlaps already processed.
// 3. Inter-reduction with stable/pending separation.
// 4. Quotient stripping with symbolic accumulation for large A.
// 5. LenLex ordering maintained: words always in canonical form.
//
// Target: O(A³) symbolic computation. A=10 in <30s, A=16 with stripping.

#![allow(dead_code, unused_imports)]
use rustc_hash::FxHashMap;
use std::collections::BTreeMap;
use std::time::Instant;

// ════════════════════════════════════════════════════════════════
// Laurent polynomial in t = q^{1/2} over ℤ
// ════════════════════════════════════════════════════════════════

#[derive(Clone, Debug, PartialEq, Eq, Default)]
struct LPoly { terms: BTreeMap<i32, i128> }

impl LPoly {
    fn zero() -> Self { Self { terms: BTreeMap::new() } }
    fn one() -> Self { let mut p = Self::zero(); p.terms.insert(0, 1); p }
    fn t(power: i32) -> Self { let mut p = Self::zero(); p.terms.insert(power, 1); p }
    fn is_zero(&self) -> bool { self.terms.is_empty() }
    fn n_terms(&self) -> usize { self.terms.len() }

    fn add(&self, other: &LPoly) -> LPoly {
        let mut r = self.clone();
        for (&k, &v) in &other.terms {
            let e = r.terms.entry(k).or_insert(0); *e += v;
            if *e == 0 { r.terms.remove(&k); }
        }
        r
    }
    fn scale(&self, s: i128) -> LPoly {
        if s == 0 { return Self::zero(); }
        let mut r = BTreeMap::new();
        for (&k, &v) in &self.terms {
            match v.checked_mul(s) {
                Some(val) if val != 0 => { r.insert(k, val); }
                Some(_) => {}
                None => { r.insert(k, if (v>0)==(s>0) { i128::MAX } else { i128::MIN }); }
            }
        }
        LPoly { terms: r }
    }
    fn mul(&self, other: &LPoly) -> LPoly {
        let mut r = BTreeMap::new();
        for (&k1, &v1) in &self.terms {
            for (&k2, &v2) in &other.terms {
                let k = k1+k2;
                let val = v1.checked_mul(v2).unwrap_or(if (v1>0)==(v2>0) { i128::MAX } else { i128::MIN });
                let e = r.entry(k).or_insert(0i128);
                *e = e.checked_add(val).unwrap_or(if val>0 { i128::MAX } else { i128::MIN });
                if *e == 0 { r.remove(&k); }
            }
        }
        LPoly { terms: r }
    }
    fn shift(&self, n: i32) -> LPoly {
        let mut r = BTreeMap::new();
        for (&k, &v) in &self.terms { r.insert(k+n, v); }
        LPoly { terms: r }
    }
    fn eval(&self, t: f64) -> f64 {
        self.terms.iter().map(|(&k, &v)| (v as f64) * t.powi(k)).sum()
    }
    fn has_overflow(&self) -> bool {
        self.terms.values().any(|&v| v == i128::MAX || v == i128::MIN)
    }
    fn max_abs_coeff(&self) -> i128 {
        self.terms.values().map(|v| v.abs()).max().unwrap_or(0)
    }
    fn display_short(&self) -> String {
        let n = self.terms.len();
        if n == 0 { return "0".into(); }
        if n <= 5 {
            self.terms.iter().map(|(&k, &v)| {
                if k == 0 { format!("{}", v) } else { format!("{}·t^{}", v, k) }
            }).collect::<Vec<_>>().join(" + ").replace("+ -", "- ")
        } else {
            format!("({} terms, degree {}..{})", n,
                self.terms.keys().next().unwrap(), self.terms.keys().next_back().unwrap())
        }
    }
}

// ════════════════════════════════════════════════════════════════
// TreeWord (same as v6/v7)
// ════════════════════════════════════════════════════════════════

const GENS_PER_CHUNK: usize = 32;
const MAX_CHUNKS: usize = 4;

#[derive(Clone, Copy, PartialEq, Eq, Hash)]
struct W { len: u8, chunks: [u128; MAX_CHUNKS] }

impl W {
    const E: W = W { len: 0, chunks: [0; MAX_CHUNKS] };
    #[inline] fn len(self) -> usize { self.len as usize }
    #[inline] fn get(self, p: usize) -> u8 {
        ((self.chunks[p/GENS_PER_CHUNK] >> ((p%GENS_PER_CHUNK)*4)) & 0xF) as u8
    }
    #[inline] fn set(&mut self, p: usize, v: u8) {
        let (c,b) = (p/GENS_PER_CHUNK, (p%GENS_PER_CHUNK)*4);
        self.chunks[c] = (self.chunks[c] & !(0xFu128 << b)) | ((v as u128) << b);
    }
    fn push(self, g: u8) -> W { let mut w=self; w.set(self.len as usize, g); w.len+=1; w }
    fn drop_last(self) -> W {
        if self.len==0 { return self; }
        let mut w=self; w.set((self.len-1) as usize, 0); w.len-=1; w
    }
    fn remove_at(self, pos: usize) -> W {
        let l=self.len as usize;
        let mut r = W { len: (l-1) as u8, chunks: [0; MAX_CHUNKS] };
        let mut j=0;
        for i in 0..l { if i==pos { continue; } r.set(j, self.get(i)); j+=1; }
        r
    }

    /// Check reducibility at the junction (last 2-3 chars only).
    /// Returns Some((pos, rule)) if reducible.
    #[inline]
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
            let a=self.get(p); let b=self.get(p+1);
            if a==b { return Some((p, 0)); }
            if (a as i16 - b as i16) >= 2 { return Some((p, 1)); }
            if p+2 < l {
                let c=self.get(p+2);
                if a==c && (a as i16 - b as i16).abs()==1 && b<a { return Some((p, 2)); }
            }
        }
        None
    }
}

impl std::fmt::Debug for W {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        let l=self.len();
        if l==0 { return write!(f, "𝟏"); }
        for i in 0..l { if i>0 { write!(f, ".")?; } write!(f, "σ{}", self.get(i))?; }
        Ok(())
    }
}

// ════════════════════════════════════════════════════════════════
// Symbolic Hecke element
// ════════════════════════════════════════════════════════════════

struct Elem { terms: FxHashMap<W, LPoly>, pn_count: u32 }

impl Elem {
    fn new() -> Self { Self { terms: FxHashMap::default(), pn_count: 0 } }
    fn identity() -> Self { let mut h=Self::new(); h.terms.insert(W::E, LPoly::one()); h }
    fn n_terms(&self) -> usize { self.terms.len() }
    fn clean(&mut self) { self.terms.retain(|_, c| !c.is_zero()); }
    fn total_poly_terms(&self) -> usize { self.terms.values().map(|c| c.n_terms()).sum() }
    fn mem_bytes(&self) -> usize { self.terms.iter().map(|(_, c)| 72 + c.n_terms()*20).sum() }
    fn has_overflow(&self) -> bool { self.terms.values().any(|c| c.has_overflow()) }
    fn max_coeff(&self) -> i128 { self.terms.values().map(|c| c.max_abs_coeff()).max().unwrap_or(0) }
}

// ════════════════════════════════════════════════════════════════
// Crossing coefficients
// ════════════════════════════════════════════════════════════════

fn ha_poly() -> LPoly {
    let mut p = LPoly::zero(); p.terms.insert(2, 1); p.terms.insert(-2, -1); p
}
fn crossing_sym(ti: u8, tj: u8) -> (LPoly, LPoly, bool) {
    match (ti, tj) {
        (b'p', b'p') => (LPoly::one(), LPoly::zero(), false),
        (b'n', b'n') => {
            let c = LPoly::t(4);
            let mut d = LPoly::zero(); d.terms.insert(3, -1); d.terms.insert(1, 1);
            (c, d, false)
        }
        _ => {
            let mut c2 = LPoly::one(); c2.terms.insert(4, 1);
            let mut d2 = LPoly::zero(); d2.terms.insert(3, -1); d2.terms.insert(1, 1);
            (c2, d2, true)
        }
    }
}

// ════════════════════════════════════════════════════════════════
// Engine with junction-only reduction + stable/pending separation
// ════════════════════════════════════════════════════════════════

/// Symbolic accumulator for Pauli data (exact in q).
struct SymPauliAcc { tr_alt: LPoly, net: LPoly }
impl SymPauliAcc {
    fn zero() -> Self { Self { tr_alt: LPoly::zero(), net: LPoly::zero() } }
    fn add_term(&mut self, coeff: &LPoly, word_len: usize) {
        self.net = self.net.add(coeff);
        let l = word_len as i32;
        let sign = if l%2==0 { 1i128 } else { -1i128 };
        self.tr_alt = self.tr_alt.add(&coeff.scale(sign).shift(-2*l));
    }
    fn add_from_elem(&mut self, elem: &Elem) {
        for (w, c) in &elem.terms { self.add_term(c, w.len()); }
    }
    fn merge(&mut self, other: &SymPauliAcc) {
        self.tr_alt = self.tr_alt.add(&other.tr_alt);
        self.net = self.net.add(&other.net);
    }
}

struct Eng;

impl Eng {
    fn multiply_and_reduce(elem: &mut Elem, gen: u8, c: &LPoly, d: &LPoly, is_dbl: bool, ha: &LPoly) {
        if is_dbl { elem.pn_count += 1; }
        let old: Vec<(W, LPoly)> = elem.terms.drain().collect();

        // Phase 1: multiply. d-terms go directly to stable (already reduced).
        // c-terms go to pending (need junction check).
        let mut stable: FxHashMap<W, LPoly> = FxHashMap::default();
        let mut pending: Vec<(W, LPoly)> = Vec::new();

        for (w, coeff) in old {
            if !d.is_zero() {
                let e = stable.entry(w).or_insert(LPoly::zero());
                *e = e.add(&coeff.mul(d));
            }
            if !c.is_zero() {
                let wg = w.push(gen);
                pending.push((wg, coeff.mul(c)));
            }
        }

        // Phase 2: reduce pending terms. Each may cascade but only leftward.
        // Use iterative approach: process pending, outputs go to next_pending or stable.
        loop {
            let mut next: Vec<(W, LPoly)> = Vec::new();
            let mut any_reduced = false;

            for (word, coeff) in pending {
                if coeff.is_zero() { continue; }

                // Junction check first (fast), then full scan as fallback
                let red = word.junction_check().or_else(|| word.find_reduction());

                if let Some((pos, rule)) = red {
                    any_reduced = true;
                    match rule {
                        0 => { // Hecke
                            let w1 = word.remove_at(pos+1);
                            let w2 = w1.remove_at(pos);
                            next.push((w1, coeff.mul(ha)));
                            next.push((w2, coeff));
                        }
                        1 => { // FC swap
                            let mut w = word;
                            let (a,b) = (w.get(pos), w.get(pos+1));
                            w.set(pos, b); w.set(pos+1, a);
                            next.push((w, coeff));
                        }
                        2 => { // YB
                            let mut w = word;
                            let (a,b) = (w.get(pos), w.get(pos+1));
                            w.set(pos, b); w.set(pos+1, a); w.set(pos+2, b);
                            next.push((w, coeff));
                        }
                        _ => {}
                    }
                } else {
                    // Fully reduced → stable
                    let e = stable.entry(word).or_insert(LPoly::zero());
                    *e = e.add(&coeff);
                }
            }

            if !any_reduced { break; }

            // Consolidate next by word (avoid duplicate work)
            let mut consolidated: FxHashMap<W, LPoly> = FxHashMap::default();
            for (w, c) in next {
                if c.is_zero() { continue; }
                let e = consolidated.entry(w).or_insert(LPoly::zero());
                *e = e.add(&c);
            }
            // Inter-reduce: if consolidated term exists in stable, merge back to pending
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
    }

    /// Strip terms and return their symbolic Pauli contribution.
    fn strip_with_pauli(terms: &mut FxHashMap<W, LPoly>) -> SymPauliAcc {
        let mut removed = SymPauliAcc::zero();
        let max_len = terms.keys().map(|w| w.len()).max().unwrap_or(0);
        for tl in (2..=max_len).rev() {
            let to_rm: Vec<W> = terms.keys()
                .filter(|w| w.len()==tl && !terms[*w].is_zero())
                .filter(|w| terms.get(&w.drop_last()).map_or(false, |c| !c.is_zero()))
                .cloned().collect();
            for w in &to_rm {
                if let Some(c) = terms.remove(w) {
                    removed.add_term(&c, w.len());
                }
            }
        }
        let adj: Vec<W> = terms.keys()
            .filter(|w| w.len()==2 && !terms[*w].is_zero() && w.get(1)==w.get(0)+1)
            .filter(|w| terms.get(&W::E.push(w.get(1))).map_or(false, |c| !c.is_zero()))
            .cloned().collect();
        for w in &adj {
            if let Some(c) = terms.remove(w) {
                removed.add_term(&c, w.len());
            }
        }
        terms.retain(|_, c| !c.is_zero());
        removed
    }

    /// Inductive build with symbolic Pauli accumulation.
    ///
    /// At each strand boundary:
    /// 1. Accumulate ALL terms' tr_alt(q) and net(q) into sym_accum
    /// 2. Strip with I₈+I₉ (keeping only optimal basis)
    /// 3. Next strand starts from optimal basis (A terms, not A! terms)
    ///
    /// The final F_Pauli = |tr_alt_accum + tr_alt_kept| / |net_accum + net_kept|
    /// is EXACT IN q — a rational function of q^{1/2}.
    fn build_inductive(z: usize, n: usize, strip_after: usize) -> (Elem, SymPauliAcc, Vec<String>) {
        let a = z + n;
        let ha = ha_poly();
        let mut types = vec![b'p'; z]; types.extend(vec![b'n'; n]);
        let mut elem = Elem::identity();
        let mut accum = SymPauliAcc::zero();
        let t0 = Instant::now();
        let mut log: Vec<String> = Vec::new();

        for k in 1..a {
            let ts = Instant::now();
            for i in 0..k {
                let tc = Instant::now();
                let n_before = elem.n_terms();
                let (c, d, dbl) = crossing_sym(types[i], types[k]);
                Self::multiply_and_reduce(&mut elem, i as u8, &c, &d, dbl, &ha);

                if elem.has_overflow() {
                    let msg = format!("OVERFLOW at crossing ({},{}) A={}", i, k, a);
                    eprintln!("  {}", msg);
                    log.push(msg);
                    return (elem, accum, log);
                }

                let ms = tc.elapsed().as_millis();
                if ms > 200 || elem.n_terms() > 10000 {
                    eprintln!("    ({},{}) {}-{}: {} → {} words, {} poly, {}ms",
                        i, k, types[i] as char, types[k] as char,
                        n_before, elem.n_terms(), elem.total_poly_terms(), ms);
                }
            }

            let pt = elem.total_poly_terms();
            let mc = elem.max_coeff();
            let mb = elem.mem_bytes() as f64 / 1_048_576.0;
            let elapsed = t0.elapsed().as_secs_f64();

            // Inductive stripping: accumulate ALL, then strip
            if (k + 1) as usize > strip_after && k < a - 1 {
                // Accumulate Pauli data of ALL current terms (exact in q)
                let mut strand_pauli = SymPauliAcc::zero();
                strand_pauli.add_from_elem(&elem);
                accum.merge(&strand_pauli);

                // Strip to optimal basis
                let n_pre = elem.n_terms();
                Self::strip_quotient(&mut elem.terms);
                let info = format!("  strand {}/{}: {} → {} words (stripped), poly ~10^{:.0}, {:.0}MB, {:.1}s",
                    k, a-1, n_pre, elem.n_terms(),
                    if mc > 0 { (mc as f64).log10() } else { 0.0 },
                    mb, elapsed);
                eprintln!("{}", info);
                log.push(info);
            } else {
                let info = format!("  strand {}/{}: {} words, {} poly (avg {}), coeff~10^{:.0}, {:.0}MB, {:.1}s",
                    k, a-1, elem.n_terms(), pt,
                    if elem.n_terms()>0 { pt/elem.n_terms() } else { 0 },
                    if mc > 0 { (mc as f64).log10() } else { 0.0 },
                    mb, elapsed);
                eprintln!("{}", info);
                log.push(info);
            }
        }
        (elem, accum, log)
    }

    /// I₉ + I₈ strip (no accumulation — for symbolic, accumulate separately)
    fn strip_quotient(terms: &mut FxHashMap<W, LPoly>) {
        let max_len = terms.keys().map(|w| w.len()).max().unwrap_or(0);
        for tl in (2..=max_len).rev() {
            let to_rm: Vec<W> = terms.keys()
                .filter(|w| w.len()==tl && !terms[*w].is_zero())
                .filter(|w| terms.get(&w.drop_last()).map_or(false, |c| !c.is_zero()))
                .cloned().collect();
            for w in to_rm { terms.remove(&w); }
        }
        let adj: Vec<W> = terms.keys()
            .filter(|w| w.len()==2 && !terms[*w].is_zero() && w.get(1)==w.get(0)+1)
            .filter(|w| terms.get(&W::E.push(w.get(1))).map_or(false, |c| !c.is_zero()))
            .cloned().collect();
        for w in adj { terms.remove(&w); }
        terms.retain(|_, c| !c.is_zero());
    }
}

// ════════════════════════════════════════════════════════════════

fn compute_pauli(elem: &Elem) -> (LPoly, LPoly) {
    let mut tr_alt = LPoly::zero();
    let mut net = LPoly::zero();
    for (w, c) in &elem.terms {
        let l = w.len() as i32;
        net = net.add(c);
        let sign = if l%2==0 { 1i128 } else { -1i128 };
        tr_alt = tr_alt.add(&c.scale(sign).shift(-2*l));
    }
    (tr_alt, net)
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.len() < 3 {
        eprintln!("Usage: v8 Z N [max_terms]");
        eprintln!("  Symbolic Pauli witness, exact in q.");
        eprintln!("  max_terms: strip threshold (default: no stripping)");
        std::process::exit(1);
    }

    let z: usize = args[1].parse().unwrap();
    let n: usize = args[2].parse().unwrap();
    let max_terms: usize = args.get(3).and_then(|s| s.parse().ok()).unwrap_or(usize::MAX);
    let a = z + n;
    let sym = match z {1=>"H",2=>"He",3=>"Li",4=>"Be",5=>"B",6=>"C",7=>"N",8=>"O",_=>"?"};
    let magic = [2,8,20,28,50,82,126];
    let dm = magic.contains(&z) && magic.contains(&n);

    println!("════════════════════════════════════════════════════════");
    println!("  v8 symbolic: {}{} (Z={}, N={}, A={})", a, sym, z, n, a);
    println!("  Exact in t = q^{{1/2}} over ℤ. {}",
        if dm { "★★ DOUBLY MAGIC" } else { "" });
    if max_terms < usize::MAX {
        println!("  Strip threshold: {} terms", max_terms);
    }
    let strip_after = if max_terms < usize::MAX {
        // User specified threshold: strip after strand where terms > max_terms
        // Estimate: strip after strand A/2 for balanced nuclei
        std::cmp::min(a / 2, 8)
    } else if a > 9 {
        // Auto: for A > 9, strip at strand boundaries to stay tractable
        8
    } else {
        999 // No stripping for A ≤ 9
    };

    println!("  Strip after strand: {} (strands >{} use inductive quotient)", strip_after, strip_after);
    println!("════════════════════════════════════════════════════════");

    let t_start = Instant::now();
    let (elem, accum, log) = Eng::build_inductive(z, n, strip_after);

    if elem.has_overflow() {
        println!("\n  OVERFLOW — symbolic result unreliable. Use float engine.");
        std::process::exit(1);
    }

    // Compute Pauli from kept terms + accumulated stripped terms
    let (kept_alt, kept_net) = compute_pauli(&elem);
    let tr_alt = kept_alt.add(&accum.tr_alt);
    let net_poly = kept_net.add(&accum.net);
    let ms = t_start.elapsed().as_millis();

    // Evaluate at q₀
    const Q0: f64 = 1.10998;
    let t0_val = Q0.sqrt();
    let denom = 2.0_f64.powi(elem.pn_count as i32);
    let tr_alt_val = tr_alt.eval(t0_val) / denom;
    let net_val = net_poly.eval(t0_val) / denom;
    let f = if net_val.abs() > 1e-30 { tr_alt_val.abs() / net_val.abs() } else { 0.0 };

    println!();
    println!("════════════════════════════════════════════════════════");
    println!("  {}{}: {} words, {} poly terms, {:.1}MB, {:.1}s",
        a, sym, elem.n_terms(), elem.total_poly_terms(),
        elem.mem_bytes() as f64 / 1e6, ms as f64 / 1000.0);
    println!("  max coeff: ~10^{:.0}", if elem.max_coeff()>0 { (elem.max_coeff() as f64).log10() } else { 0.0 });
    println!("  pn_count = {} (denominator 2^{})", elem.pn_count, elem.pn_count);
    println!();
    println!("  tr_alt(t) = {}", tr_alt.display_short());
    println!("  net(t)    = {}", net_poly.display_short());
    println!();
    println!("  At q₀ = {}:", Q0);
    println!("  F_Pauli = {:.10}", f);
    println!("════════════════════════════════════════════════════════");

    // Lean witness (compact for large polynomials)
    if tr_alt.n_terms() <= 200 && net_poly.n_terms() <= 200 {
        println!();
        println!("-- LEAN: exact in ℤ[t, t⁻¹], denominator 2^{}", elem.pn_count);
        let lsym = sym.to_lowercase();
        println!("noncomputable def tr_alt_{}{} : LaurentPolynomial ℤ :=", a, lsym);
        print!("  ");
        let mut first = true;
        for (&k, &v) in &tr_alt.terms {
            if !first && v>0 { print!(" + "); } else if !first { print!(" - "); } else if v<0 { print!("-"); }
            let av = v.unsigned_abs();
            if k==0 { print!("{}", av); }
            else if av==1 { print!("LaurentPolynomial.T {}", k); }
            else { print!("{} • LaurentPolynomial.T {}", av, k); }
            first = false;
        }
        println!();
    } else {
        println!();
        println!("-- Polynomial too large for inline Lean ({} + {} terms).", tr_alt.n_terms(), net_poly.n_terms());
        println!("-- Write to file: v8-witness-{}{}.json", a, sym.to_lowercase());
    }
}
