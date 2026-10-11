// Excised from tools/hecke-engine/src/bin/v9.rs at commit bd6e0dcb86 (bean qou-m7py, issue #7685).
// Lines 405-501 (SymPauliAcc incl. the three tr_markov functions):

// ════════════════════════════════════════════════════════════════
// Pauli accumulator (BigInt version)
// ════════════════════════════════════════════════════════════════

#[derive(Clone)]
struct SymPauliAcc {
    tr_alt: LPoly,
    net: LPoly,
    tr_markov: LPoly,  // Markov trace: Σ c_w × z^ℓ(w) where z = 1/(√q + 1/√q)
    net_by_len: Vec<LPoly>,
}

impl SymPauliAcc {
    fn zero() -> Self { Self { tr_alt: LPoly::zero(), net: LPoly::zero(), tr_markov: LPoly::zero(), net_by_len: Vec::new() } }

    fn add_term(&mut self, coeff: &LPoly, word_len: usize) {
        self.net = self.net.add(coeff);
        let l = word_len as i64;
        let sign = if l % 2 == 0 { 1i64 } else { -1i64 };
        self.tr_alt = self.tr_alt.add(&coeff.scale_i64(sign).shift(-2 * word_len as i32));
        // Markov trace: weight by z^ℓ
        // z = 1/(t + t⁻¹) where t = q^{1/2}
        // z^ℓ = 1/(t + t⁻¹)^ℓ
        // In Laurent polynomial arithmetic: multiply coeff by (t+t⁻¹)^{-ℓ}
        // But (t+t⁻¹)^{-ℓ} is NOT a Laurent polynomial.
        // Instead: store Σ c_w × (t+t⁻¹)^{max_len - ℓ(w)} and divide by (t+t⁻¹)^{max_len} later.
        // OR: just compute tr_M at the end from net_by_len.
        // Per-length tracking
        while self.net_by_len.len() <= word_len {
            self.net_by_len.push(LPoly::zero());
        }
        self.net_by_len[word_len] = self.net_by_len[word_len].add(coeff);
    }

    fn compute_tr_markov_poly(&self) -> (LPoly, usize) {
        // tr_M = Σ_ℓ net_by_len[ℓ] / (t + t⁻¹)^ℓ
        // Cleared form: tr_M_cleared = Σ_ℓ net_by_len[ℓ] × (t + t⁻¹)^{L-ℓ}
        // where L = max word length
        // Then tr_M = tr_M_cleared / (t + t⁻¹)^L
        //
        // (t + t⁻¹) as Laurent poly: T^1 + T^{-1}
        // (t + t⁻¹)^k computed by repeated multiplication

        let max_len = self.net_by_len.len().saturating_sub(1);

        // Precompute (t + t⁻¹)^k for k = 0..max_len
        let t_plus_tinv = {
            let mut p = LPoly::zero();
            p.terms.insert(1, BigInt::one());   // t^1
            p.terms.insert(-1, BigInt::one());  // t^{-1}
            p
        };

        let mut powers = vec![LPoly::one()]; // (t+t⁻¹)^0 = 1
        for _ in 1..=max_len {
            let prev = powers.last().unwrap();
            powers.push(prev.mul(&t_plus_tinv));
        }

        // tr_M_cleared = Σ_ℓ net_by_len[ℓ] × (t+t⁻¹)^{max_len - ℓ}
        let mut cleared = LPoly::zero();
        for (ell, poly) in self.net_by_len.iter().enumerate() {
            if poly.is_zero() { continue; }
            let power_idx = max_len - ell;
            if power_idx < powers.len() {
                cleared = cleared.add(&poly.mul(&powers[power_idx]));
            }
        }

        (cleared, max_len)
    }

    fn compute_tr_markov_f64(&self, t0: f64, pn_count: u32) -> f64 {
        let z = 1.0 / (t0 + 1.0/t0);
        let denom = 2.0_f64.powi(pn_count as i32);
        let mut tr_m = 0.0;
        for (ell, poly) in self.net_by_len.iter().enumerate() {
            let val = poly.eval_f64(t0);
            tr_m += val * z.powi(ell as i32);
        }
        tr_m / denom
    }

    fn compute_tr_markov_mpfr(&self, t0_f64: f64, pn_count: u32, prec: u32) -> MpFloat {
        let t0 = MpFloat::with_val(prec, t0_f64);
        let z = MpFloat::with_val(prec, 1.0) / (MpFloat::with_val(prec, &t0 + MpFloat::with_val(prec, 1.0) / &t0));
        let denom = MpFloat::with_val(prec, 2.0).pow(pn_count as u32);
        let mut tr_m = MpFloat::with_val(prec, 0.0);
        let mut z_pow = MpFloat::with_val(prec, 1.0);
        for poly in &self.net_by_len {
            let val = poly.eval_mpfr(t0_f64, prec);
            tr_m += MpFloat::with_val(prec, &val * &z_pow);
            z_pow = MpFloat::with_val(prec, &z_pow * &z);
        }
        MpFloat::with_val(prec, tr_m / denom)
    }

// main(), lines 899-909:
    // Markov trace: tr_M = Σ_ℓ net_by_len[ℓ] × z^ℓ
    let tr_m_val = if mc < 300.0 {
        total.compute_tr_markov_f64(t0_val, elem.pn_count)
    } else {
        let prec = (mc as u32 + 100) * 4;
        total.compute_tr_markov_mpfr(t0_val, elem.pn_count, prec).to_f64()
    };
    println!("  tr_M(q₀)   = {:.10e}  (Markov trace of full NF)", tr_m_val);
    let (tr_m_cleared, tr_m_L) = total.compute_tr_markov_poly();
    println!("  tr_M_cleared: {} terms, denom=(t+t⁻¹)^{}", tr_m_cleared.terms.len(), tr_m_L);
    println!("  tr_M(t) = tr_M_cleared(t) / (t+t⁻¹)^{} / 2^{}", tr_m_L, elem.pn_count);

// WitnessCertificate fields, lines 971-979:
        tr_markov_f64: if tr_m_val.is_finite() { Some(tr_m_val) } else { None },
        tr_markov_cleared: {
            let (cleared, _) = total.compute_tr_markov_poly();
            SparsePoly::from_btree(&cleared.terms)
        },
        tr_markov_denom_power: {
            let (_, l) = total.compute_tr_markov_poly();
            l
        },

// src/certificate.rs fields:
92:    pub tr_markov_f64: Option<f64>,        // Markov trace of full NF at q₀
93:    pub tr_markov_cleared: SparsePoly,     // tr_M × (t+t⁻¹)^L — symbolic in t
94:    pub tr_markov_denom_power: usize,      // L: divide by (t+t⁻¹)^L to get tr_M
