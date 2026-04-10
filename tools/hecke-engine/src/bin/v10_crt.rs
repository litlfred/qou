// v10: CRT modular engine — u64 arithmetic, no BigInt.
//
// Computes Hecke NF mod K primes, outputs per-term CRT residues.
// Python reconstructs exact BigInt coefficients and evaluates f_pauli.
//
// Each prime: pure u64 arithmetic. O(1) per multiply.
// Expected 10-100× speedup over BigInt (v9).
//
// Usage:
//   hecke-crt Z N [strip_threshold]

use rustc_hash::FxHashMap;
use std::collections::BTreeMap;
use std::time::Instant;

// ════════════════════════════════════════════════════════════════
// Modular arithmetic
// ════════════════════════════════════════════════════════════════

const PRIMES: [u64; 4] = [
    1_000_000_007, 1_000_000_009, 998_244_353, 985_661_441,
];

fn mod_add(a: u64, b: u64, p: u64) -> u64 {
    ((a as u128 + b as u128) % p as u128) as u64
}
fn mod_sub(a: u64, b: u64, p: u64) -> u64 {
    if a >= b { a - b } else { p - b + a }
}
fn mod_mul(a: u64, b: u64, p: u64) -> u64 {
    ((a as u128 * b as u128) % p as u128) as u64
}

// ════════════════════════════════════════════════════════════════
// Laurent polynomial mod p
// ════════════════════════════════════════════════════════════════

#[derive(Clone)]
struct MP {
    t: BTreeMap<i32, u64>,
    p: u64,
}

impl MP {
    fn zero(p: u64) -> Self { Self { t: BTreeMap::new(), p } }
    fn one(p: u64) -> Self { let mut m = Self::zero(p); m.t.insert(0, 1); m }
    fn is_zero(&self) -> bool { self.t.is_empty() }
    fn n_terms(&self) -> usize { self.t.len() }

    fn add(&self, o: &MP) -> MP {
        let mut r = self.t.clone();
        for (k, v) in &o.t {
            let e = r.entry(*k).or_insert(0);
            *e = mod_add(*e, *v, self.p);
            if *e == 0 { r.remove(k); }
        }
        MP { t: r, p: self.p }
    }
    fn sub(&self, o: &MP) -> MP {
        let mut r = self.t.clone();
        for (k, v) in &o.t {
            let e = r.entry(*k).or_insert(0);
            *e = mod_sub(*e, *v, self.p);
            if *e == 0 { r.remove(k); }
        }
        MP { t: r, p: self.p }
    }
    fn mul(&self, o: &MP) -> MP {
        let mut r: BTreeMap<i32, u64> = BTreeMap::new();
        for (k1, v1) in &self.t {
            for (k2, v2) in &o.t {
                let k = k1 + k2;
                let val = mod_mul(*v1, *v2, self.p);
                let e = r.entry(k).or_insert(0);
                *e = mod_add(*e, val, self.p);
                if *e == 0 { r.remove(&k); }
            }
        }
        MP { t: r, p: self.p }
    }
    fn neg(&self) -> MP {
        let mut r = BTreeMap::new();
        for (k, v) in &self.t { r.insert(*k, mod_sub(0, *v, self.p)); }
        MP { t: r, p: self.p }
    }
    fn terms_vec(&self) -> Vec<(i32, u64)> {
        self.t.iter().map(|(k, v)| (*k, *v)).collect()
    }
}

// ════════════════════════════════════════════════════════════════
// Compact word (same as v9)
// ════════════════════════════════════════════════════════════════

#[derive(Clone, Copy, PartialEq, Eq, Hash)]
struct W { d: [u64; 8], n: u8 }
impl W {
    const E: W = W { d: [0; 8], n: 0 };
    fn len(self) -> usize { self.n as usize }
    fn get(self, i: usize) -> u8 { ((self.d[i/8] >> ((i%8)*8)) & 0xFF) as u8 }
    fn set(&mut self, i: usize, v: u8) {
        self.d[i/8] &= !(0xFF << ((i%8)*8));
        self.d[i/8] |= (v as u64) << ((i%8)*8);
    }
    fn push(mut self, v: u8) -> W {
        let i = self.n as usize;
        if i >= 64 { return self; }
        self.set(i, v); self.n += 1; self
    }
    fn remove_at(self, pos: usize) -> W {
        let mut r = W::E;
        for i in 0..self.len() { if i != pos { r = r.push(self.get(i)); } }
        r
    }
    fn drop_last(self) -> W { let mut r = self; r.n -= 1; r }

    fn find_red(self) -> Option<(usize, u8)> {
        let n = self.len();
        for p in 0..n.saturating_sub(1) {
            let a = self.get(p); let b = self.get(p+1);
            if a == b { return Some((p, 0)); }
            if p+2 < n {
                let c = self.get(p+2);
                if a == c && (a as i8 - b as i8).unsigned_abs() == 1 {
                    if (b,a,b) < (a,b,a) { return Some((p, 2)); }
                }
            }
            if (a as i8 - b as i8).unsigned_abs() >= 2 && a > b { return Some((p, 1)); }
        }
        None
    }
    fn junction(self) -> Option<(usize, u8)> {
        let n = self.len();
        if n < 2 { return None; }
        let p = n - 2;
        let (a, b) = (self.get(p), self.get(p+1));
        if a == b { return Some((p, 0)); }
        if n >= 3 {
            let c = self.get(p-1);
            if c == b && (a as i8 - c as i8).unsigned_abs() == 1 { return Some((p-1, 2)); }
        }
        if (a as i8 - b as i8).unsigned_abs() >= 2 && a > b { return Some((p, 1)); }
        None
    }
}

// ════════════════════════════════════════════════════════════════
// Hecke element mod p
// ════════════════════════════════════════════════════════════════

fn ha_mod(p: u64) -> MP {
    let mut h = MP::zero(p);
    h.t.insert(2, 1); h.t.insert(-2, p - 1);
    h
}

fn crossing(ti: u8, tj: u8, p: u64) -> (MP, MP, bool) {
    let ha = ha_mod(p);
    match (ti, tj) {
        (b'p', b'p') => (MP::one(p), MP::zero(p), false),
        (b'n', b'n') => (MP::one(p), ha.neg(), false),
        _ => {
            let mut c2 = MP::zero(p); c2.t.insert(0, 2);
            (c2, ha.neg(), true)
        }
    }
}

fn mul_reduce(terms: &mut FxHashMap<W, MP>, gen: u8, c: &MP, d: &MP, ha: &MP, p: u64) {
    let old: Vec<(W, MP)> = terms.drain().collect();
    let mut stable: FxHashMap<W, MP> = FxHashMap::default();
    let mut pending: Vec<(W, MP)> = Vec::new();

    for (w, coeff) in old {
        if !d.is_zero() {
            let e = stable.entry(w).or_insert(MP::zero(p));
            *e = e.add(&coeff.mul(d));
        }
        if !c.is_zero() { pending.push((w.push(gen), coeff.mul(c))); }
    }

    let mut iters = 0u32;
    loop {
        iters += 1;
        if iters > 50000 { break; }
        let mut next: Vec<(W, MP)> = Vec::new();
        let mut any = false;
        for (w, co) in pending {
            if co.is_zero() { continue; }
            let red = w.junction().or_else(|| w.find_red());
            if let Some((pos, rule)) = red {
                any = true;
                match rule {
                    0 => {
                        let w1 = w.remove_at(pos+1);
                        let w2 = w1.remove_at(pos);
                        next.push((w1, co.mul(ha)));
                        next.push((w2, co));
                    }
                    1 => {
                        let mut ww = w;
                        let (a, b) = (ww.get(pos), ww.get(pos+1));
                        ww.set(pos, b); ww.set(pos+1, a);
                        next.push((ww, co));
                    }
                    2 => {
                        let mut ww = w;
                        let (a, b) = (ww.get(pos), ww.get(pos+1));
                        ww.set(pos, b); ww.set(pos+1, a); ww.set(pos+2, b);
                        next.push((ww, co));
                    }
                    _ => {}
                }
            } else {
                let e = stable.entry(w).or_insert(MP::zero(p));
                *e = e.add(&co);
            }
        }
        if !any { break; }
        let mut cons: FxHashMap<W, MP> = FxHashMap::default();
        for (w, c) in next {
            if c.is_zero() { continue; }
            let e = cons.entry(w).or_insert(MP::zero(p));
            *e = e.add(&c);
        }
        pending = Vec::new();
        for (w, c) in cons {
            if c.is_zero() { continue; }
            if let Some(ex) = stable.remove(&w) {
                let m = ex.add(&c);
                if !m.is_zero() && w.find_red().is_some() { pending.push((w, m)); }
                else if !m.is_zero() { stable.insert(w, m); }
            } else { pending.push((w, c)); }
        }
    }
    stable.retain(|_, c| !c.is_zero());
    *terms = stable;
}

fn strip(terms: &mut FxHashMap<W, MP>, p: u64) -> (MP, MP) {
    let mut tr_alt = MP::zero(p);
    let mut net = MP::zero(p);
    for _ in 0..500 {
        let mut any = false;
        let ml = terms.keys().map(|w| w.len()).max().unwrap_or(0);
        for tl in (2..=ml).rev() {
            let rm: Vec<W> = terms.keys()
                .filter(|w| w.len() == tl && !terms[*w].is_zero())
                .filter(|w| terms.get(&w.drop_last()).map_or(false, |c| !c.is_zero()))
                .cloned().collect();
            for w in &rm {
                if let Some(c) = terms.remove(w) {
                    if w.len() % 2 == 0 { tr_alt = tr_alt.add(&c); }
                    else { tr_alt = tr_alt.sub(&c); }
                    net = net.add(&c);
                    any = true;
                }
            }
        }
        let adj: Vec<W> = terms.keys()
            .filter(|w| w.len() == 2 && !terms[*w].is_zero() && w.get(1) == w.get(0) + 1)
            .filter(|w| terms.get(&W::E.push(w.get(1))).map_or(false, |c| !c.is_zero()))
            .cloned().collect();
        for w in &adj {
            if let Some(c) = terms.remove(w) {
                if w.len() % 2 == 0 { tr_alt = tr_alt.add(&c); }
                else { tr_alt = tr_alt.sub(&c); }
                net = net.add(&c);
                any = true;
            }
        }
        if !any { break; }
    }
    terms.retain(|_, c| !c.is_zero());
    (tr_alt, net)
}

// ════════════════════════════════════════════════════════════════
// Build nucleus mod p — returns per-term CRT residues
// ════════════════════════════════════════════════════════════════

fn build(z: usize, n: usize, p: u64, threshold: usize) -> (MP, MP, u32, usize) {
    let a = z + n;
    let ha = ha_mod(p);
    let mut types = vec![b'p'; z];
    types.extend(vec![b'n'; n]);
    let mut terms: FxHashMap<W, MP> = FxHashMap::default();
    terms.insert(W::E, MP::one(p));
    let mut pn_count = 0u32;
    let mut acc_alt = MP::zero(p);
    let mut acc_net = MP::zero(p);

    let strip_from = if a <= 10 { 999 } else { 2 };

    for k in 1..a {
        for i in 0..k {
            let (c, d, dbl) = crossing(types[i], types[k], p);
            if dbl { pn_count += 1; }
            mul_reduce(&mut terms, i as u8, &c, &d, &ha, p);

            if a > 16 || (k >= strip_from && terms.len() > threshold) {
                let (ta, nt) = strip(&mut terms, p);
                acc_alt = acc_alt.add(&ta);
                acc_net = acc_net.add(&nt);
            }
        }
        if k + 1 > strip_from {
            let (ta, nt) = strip(&mut terms, p);
            acc_alt = acc_alt.add(&ta);
            acc_net = acc_net.add(&nt);
        }
    }

    // Final: add remaining
    for (w, c) in &terms {
        if w.len() % 2 == 0 { acc_alt = acc_alt.add(c); }
        else { acc_alt = acc_alt.sub(c); }
        acc_net = acc_net.add(c);
    }

    (acc_alt, acc_net, pn_count, terms.len())
}

// ════════════════════════════════════════════════════════════════
// Main: run all primes, output CRT residues
// ════════════════════════════════════════════════════════════════

fn element_symbol(z: usize) -> &'static str {
    match z {
        1=>"h",2=>"he",3=>"li",4=>"be",5=>"b",6=>"c",7=>"n",8=>"o",
        9=>"f",10=>"ne",11=>"na",12=>"mg",13=>"al",14=>"si",15=>"p",
        16=>"s",17=>"cl",18=>"ar",19=>"k",20=>"ca",
        21=>"sc",22=>"ti",23=>"v",24=>"cr",25=>"mn",26=>"fe",
        27=>"co",28=>"ni",29=>"cu",30=>"zn",_=>"?"
    }
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.len() < 3 {
        eprintln!("Usage: hecke-crt Z N [threshold]");
        std::process::exit(1);
    }
    let z: usize = args[1].parse().unwrap();
    let n: usize = args[2].parse().unwrap();
    let threshold: usize = args.get(3).and_then(|s| s.parse().ok()).unwrap_or(500);
    let a = z + n;
    let sym = element_symbol(z);

    eprintln!("hecke-crt v10 — CRT modular engine");
    eprintln!("  {}{} (Z={}, N={}, A={}), threshold={}", a, sym, z, n, a, threshold);

    let t0 = Instant::now();

    // Collect CRT residues for tr_alt and net from all primes
    let mut all_alt: Vec<Vec<(i32, u64)>> = Vec::new();
    let mut all_net: Vec<Vec<(i32, u64)>> = Vec::new();
    let mut pn_count = 0u32;

    for (pi, &p) in PRIMES.iter().enumerate() {
        let pt = Instant::now();
        let (alt, net, pn, nw) = build(z, n, p, threshold);
        let elapsed = pt.elapsed().as_secs_f64();
        pn_count = pn;
        eprintln!("  prime[{}] p={}: alt={} terms, net={} terms, {} words, {:.2}s",
            pi, p, alt.n_terms(), net.n_terms(), nw, elapsed);
        all_alt.push(alt.terms_vec());
        all_net.push(net.terms_vec());
    }

    let total = t0.elapsed().as_secs_f64();
    eprintln!("  Total: {:.2}s, pn_count={}", total, pn_count);

    // Output JSON with CRT residues
    // The Python side will reconstruct exact coefficients via CRT
    let cert = serde_json::json!({
        "isotope": { "z": z, "n": n, "a": a, "symbol": sym },
        "engine": { "name": "hecke-crt", "version": "0.10.0" },
        "primes": PRIMES,
        "pn_count": pn_count,
        "tr_alt_crt": all_alt,
        "net_crt": all_net,
        "elapsed_seconds": total,
    });

    let fname = format!("certificate-{}{}-crt.json", a, sym);
    std::fs::write(&fname, serde_json::to_string(&cert).unwrap()).unwrap();
    eprintln!("  Certificate: {}", fname);
}
