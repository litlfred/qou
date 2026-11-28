//! Streaming Gröbner–Shirshov accumulation and inductive Markov tower peeling
//! $H_n(q) \to H_{n-1}(q) \to \dots \to H_1(q) = R$.
//!
//! Multiplying a braid or Hecke expression one factor at a time while reducing to the
//! Bokut–Shiao Gröbner–Shirshov normal form keeps intermediate support bounded by $n!$.
//! Because every reduced Coxeter word in $S_k$ uses the top generator $\sigma_{k-2}$ at most
//! once, peeling $H_k(q) \to H_{k-1}(q)$ replaces each $\sigma_{k-2}$-containing word
//! $u\,\sigma_{k-2}\,v$ ($u, v \in H_{k-1}$) by $z \cdot \operatorname{nf}_{H_{k-1}}(v\,u)$
//! (via cyclic trace invariance $\operatorname{tr}(u\sigma_{k-2}v) = \operatorname{tr}(vu\sigma_{k-2})$
//! and the Markov property), and passes $\sigma_{k-2}$-free words down unchanged.

use crate::free_alg::FreeAlg;
use crate::hecke::BokutShiaoHecke;
use crate::scalar::RingScalar;
use crate::shirshov::NormalFormBasis;

/// Linear crossing factor $c\,\sigma_{\text{gen}} + d\,\mathbf{1} \in H_n(q)$.
#[derive(Clone, PartialEq, Eq, Debug)]
pub struct LinearFactor<R> {
    /// Coefficient $c$ of $\sigma_{\text{gen}}$.
    pub c: R,
    /// Coefficient $d$ of $\mathbf{1}$.
    pub d: R,
    /// 0-based Artin/Hecke generator index `0 <= gen < num_strands - 1`.
    pub gen: usize,
}

impl<R: RingScalar> LinearFactor<R> {
    /// Pure positive generator $1 \cdot \sigma_{\text{gen}}$.
    pub fn sigma(gen: usize) -> Self {
        Self {
            c: R::one(),
            d: R::zero(),
            gen,
        }
    }

    /// Balanced inverse generator $\sigma_{\text{gen}}^{-1} = \sigma_{\text{gen}} - h\,\mathbf{1}$.
    pub fn sigma_inv(gen: usize, h: &R) -> Self {
        Self {
            c: R::one(),
            d: h.neg_val(),
            gen,
        }
    }

    /// Arbitrary linear combination $c\,\sigma_{\text{gen}} + d\,\mathbf{1}$.
    pub fn new(c: R, d: R, gen: usize) -> Self {
        Self { c, d, gen }
    }

    /// Convert to a two-term `FreeAlg<usize, R>` element.
    pub fn to_free_alg(&self) -> FreeAlg<usize, R> {
        &FreeAlg::term(vec![self.gen], self.c.clone()) + &FreeAlg::scalar(self.d.clone())
    }
}

/// Streaming accumulator maintaining an element in $H_n(q)$ in Bokut–Shiao normal form
/// after each right-multiplied factor.
#[derive(Clone, Debug)]
pub struct StreamingHeckeAccumulator<R> {
    basis: BokutShiaoHecke<R>,
    state: FreeAlg<usize, R>,
    peak_support: usize,
}

impl<R: RingScalar> StreamingHeckeAccumulator<R> {
    /// Initialize at the multiplicative identity $\mathbf{1} \in H_n(q)$.
    pub fn new(num_strands: usize, h: R) -> Self {
        Self {
            basis: BokutShiaoHecke::new(num_strands, h),
            state: FreeAlg::one(),
            peak_support: 1,
        }
    }

    /// Underlying Bokut–Shiao basis.
    pub fn basis(&self) -> &BokutShiaoHecke<R> {
        &self.basis
    }

    /// Current normal-form state in $H_n(q)$.
    pub fn state(&self) -> &FreeAlg<usize, R> {
        &self.state
    }

    /// Maximum number of non-zero normal-form basis words observed across all streaming steps.
    pub fn peak_support(&self) -> usize {
        self.peak_support
    }

    /// Multiply on the right by $\sigma_{\text{gen}}$ and reduce immediately to normal form.
    pub fn push_generator(&mut self, gen: usize) {
        self.push_linear(&LinearFactor::sigma(gen));
    }

    /// Multiply on the right by $c\,\sigma_{\text{gen}} + d\,\mathbf{1}$ and reduce immediately.
    pub fn push_linear(&mut self, factor: &LinearFactor<R>) {
        let mut next = FreeAlg::zero();
        if !factor.d.is_zero() {
            next.add_scaled_assign(&self.state, &factor.d);
        }
        if !factor.c.is_zero() {
            for (w, coeff) in self.state.terms() {
                let mut w_ext = Vec::with_capacity(w.len() + 1);
                w_ext.extend_from_slice(w);
                w_ext.push(factor.gen);
                let red = self.basis.reduce_word(&w_ext);
                let scaled = coeff.mul_val(&factor.c);
                next.add_scaled_assign(&red, &scaled);
            }
        }
        self.peak_support = self.peak_support.max(next.num_terms());
        self.state = next;
    }

    /// Multiply on the right by an arbitrary `FreeAlg` element and reduce to normal form.
    pub fn push_element(&mut self, elem: &FreeAlg<usize, R>) {
        self.state = self.basis.multiply_reduced(&self.state, elem);
        self.peak_support = self.peak_support.max(self.state.num_terms());
    }

    /// Consume the accumulator and return the final normal-form element.
    pub fn into_state(self) -> FreeAlg<usize, R> {
        self.state
    }
}

/// Peel a single top generator `top_gen = k - 2` ($H_k(q) \to H_{k-1}(q)$) from an element
/// whose support uses only generators `<= top_gen`, applying cyclic invariance and the Markov
/// rule $\operatorname{tr}(u\,\sigma_{\text{top\_gen}}\,v) = z\,\operatorname{tr}(v\,u)$.
pub fn peel_top_layer<R: RingScalar>(
    elem: &FreeAlg<usize, R>,
    top_gen: usize,
    h: &R,
    z: &R,
) -> FreeAlg<usize, R> {
    // Ensure `elem` is in Bokut-Shiao normal form for H_{top_gen + 2}:
    let top_basis = BokutShiaoHecke::new(top_gen + 2, h.clone());
    let sub_basis = BokutShiaoHecke::new(top_gen + 1, h.clone());
    let nf = top_basis.reduce(elem);

    let mut out = FreeAlg::zero();
    for (w, coeff) in nf.terms() {
        match w.iter().position(|&g| g == top_gen) {
            None => {
                // Already in H_{top_gen + 1}: pass down unchanged.
                out.add_scaled_assign(&FreeAlg::word(w.clone()), coeff);
            }
            Some(pos) => {
                debug_assert!(
                    w[pos + 1..].iter().all(|&g| g < top_gen),
                    "reduced Coxeter word in S_{{k}} contains top generator at most once"
                );
                // Cyclic conjugation: tr(u * sigma_{top_gen} * v) = tr(v * u * sigma_{top_gen}) = z * tr(v * u)
                let mut vu = Vec::with_capacity(w.len() - 1);
                vu.extend_from_slice(&w[pos + 1..]);
                vu.extend_from_slice(&w[..pos]);
                let red_vu = sub_basis.reduce_word(&vu);
                let z_coeff = coeff.mul_val(z);
                out.add_scaled_assign(&red_vu, &z_coeff);
            }
        }
    }
    out
}

/// Peel an arbitrary element of $H_n(q)$ all the way down the tower
/// $H_n(q) \to H_{n-1}(q) \to \dots \to H_1(q) = R$, returning the exact scalar Markov trace
/// together with the per-level normal-form support sizes `[|H_n|, |H_{n-1}|, ..., |H_1|]`.
pub fn peel_tower_trace<R: RingScalar>(
    elem: &FreeAlg<usize, R>,
    num_strands: usize,
    h: &R,
    z: &R,
) -> (R, Vec<usize>) {
    assert!(num_strands >= 1, "num_strands must be >= 1");
    let top_basis = BokutShiaoHecke::new(num_strands, h.clone());
    let mut cur = top_basis.reduce(elem);
    let mut level_supports = Vec::with_capacity(num_strands);
    level_supports.push(cur.num_terms());

    for top_gen in (0..num_strands.saturating_sub(1)).rev() {
        cur = peel_top_layer(&cur, top_gen, h, z);
        level_supports.push(cur.num_terms());
    }

    let trace_val = cur.coeff(&[]);
    (trace_val, level_supports)
}

/// Stream a sequence of linear factors into $H_n(q)$ (with online horizon peeling whenever the
/// highest active generator never reappears in the remaining suffix) and return its exact
/// normalized Markov trace $\operatorname{tr}_M(\prod_t (c_t\sigma_{g_t} + d_t)) \in R$.
pub fn streaming_markov_trace<R: RingScalar>(
    factors: &[LinearFactor<R>],
    num_strands: usize,
    h: &R,
    z: &R,
) -> R {
    assert!(num_strands >= 1, "num_strands must be >= 1");
    if factors.is_empty() {
        return R::one();
    }

    // Compute last step index at which each generator appears, enabling online top-layer peeling:
    let max_gens = num_strands.saturating_sub(1);
    let mut last_seen: Vec<Option<usize>> = vec![None; max_gens];
    for (idx, f) in factors.iter().enumerate() {
        assert!(
            f.gen < max_gens,
            "generator {} out of range for {} strands",
            f.gen,
            num_strands
        );
        last_seen[f.gen] = Some(idx);
    }

    let mut active_top: Option<usize> = if max_gens == 0 {
        None
    } else {
        Some(max_gens - 1)
    };
    // Immediately peel any high generators that never appear in `factors` at all:
    while let Some(top) = active_top {
        if last_seen[top].is_none() {
            active_top = top.checked_sub(1);
        } else {
            break;
        }
    }

    let eff_strands = active_top.map_or(1, |g| g + 2);
    let mut state = FreeAlg::<usize, R>::one();
    let mut cur_strands = eff_strands;
    let mut cur_basis = BokutShiaoHecke::new(cur_strands, h.clone());

    for (step_idx, factor) in factors.iter().enumerate() {
        // Multiply single linear factor and reduce in current H_{cur_strands}:
        let mut next = FreeAlg::zero();
        if !factor.d.is_zero() {
            next.add_scaled_assign(&state, &factor.d);
        }
        if !factor.c.is_zero() {
            for (w, coeff) in state.terms() {
                let mut w_ext = Vec::with_capacity(w.len() + 1);
                w_ext.extend_from_slice(w);
                w_ext.push(factor.gen);
                let red = cur_basis.reduce_word(&w_ext);
                let scaled = coeff.mul_val(&factor.c);
                next.add_scaled_assign(&red, &scaled);
            }
        }
        state = next;

        // Peel any top generators whose last occurrence <= step_idx:
        while cur_strands >= 2 {
            let top_gen = cur_strands - 2;
            let done_with_top = match last_seen[top_gen] {
                None => true,
                Some(last_idx) => last_idx <= step_idx,
            };
            if done_with_top {
                state = peel_top_layer(&state, top_gen, h, z);
                cur_strands -= 1;
                cur_basis = BokutShiaoHecke::new(cur_strands, h.clone());
            } else {
                break;
            }
        }
    }

    while cur_strands >= 2 {
        let top_gen = cur_strands - 2;
        state = peel_top_layer(&state, top_gen, h, z);
        cur_strands -= 1;
    }

    state.coeff(&[])
}

/// Homogeneous division-free peel of a single top generator `top_gen = k - 2` ($H_k \to H_{k-1}$)
/// for rational Markov parameters $z = z_{\mathrm{num}} / z_{\mathrm{den}}$:
/// multiplies $\sigma_{\text{top\_gen}}$-linear words by `z_num` and $\sigma_{\text{top\_gen}}$-free
/// words by `z_den`, avoiding fraction-field GCDs entirely.
pub fn peel_top_layer_homogeneous<R: RingScalar>(
    elem: &FreeAlg<usize, R>,
    top_gen: usize,
    h: &R,
    z_num: &R,
    z_den: &R,
) -> FreeAlg<usize, R> {
    let top_basis = BokutShiaoHecke::new(top_gen + 2, h.clone());
    let sub_basis = BokutShiaoHecke::new(top_gen + 1, h.clone());
    let nf = top_basis.reduce(elem);

    let mut out = FreeAlg::zero();
    for (w, coeff) in nf.terms() {
        match w.iter().position(|&g| g == top_gen) {
            None => {
                let scaled = coeff.mul_val(z_den);
                out.add_scaled_assign(&FreeAlg::word(w.clone()), &scaled);
            }
            Some(pos) => {
                let mut vu = Vec::with_capacity(w.len() - 1);
                vu.extend_from_slice(&w[pos + 1..]);
                vu.extend_from_slice(&w[..pos]);
                let red_vu = sub_basis.reduce_word(&vu);
                let scaled = coeff.mul_val(z_num);
                out.add_scaled_assign(&red_vu, &scaled);
            }
        }
    }
    out
}

/// Stream linear factors on `num_strands` strands and perform homogeneous division-free Markov
/// tower peeling, returning exact $z_{\mathrm{den}}^{\,n-1}\,\operatorname{tr}_{M, z_{\mathrm{num}}/z_{\mathrm{den}}}(\prod_t (c_t\sigma_{g_t} + d_t)) \in R$.
pub fn streaming_markov_trace_homogeneous<R: RingScalar>(
    factors: &[LinearFactor<R>],
    num_strands: usize,
    h: &R,
    z_num: &R,
    z_den: &R,
) -> R {
    assert!(num_strands >= 1, "num_strands must be >= 1");
    if num_strands == 1 {
        return R::one();
    }
    if factors.is_empty() {
        return z_den.pow_u32((num_strands - 1) as u32);
    }

    let max_gens = num_strands - 1;
    let mut last_seen: Vec<Option<usize>> = vec![None; max_gens];
    for (idx, f) in factors.iter().enumerate() {
        assert!(f.gen < max_gens, "generator out of range");
        last_seen[f.gen] = Some(idx);
    }

    let mut peeled_unused = 0u32;
    let mut active_top: Option<usize> = Some(max_gens - 1);
    while let Some(top) = active_top {
        if last_seen[top].is_none() {
            peeled_unused += 1;
            active_top = top.checked_sub(1);
        } else {
            break;
        }
    }

    let eff_strands = active_top.map_or(1, |g| g + 2);
    let mut state = FreeAlg::<usize, R>::scalar(z_den.pow_u32(peeled_unused));
    let mut cur_strands = eff_strands;
    let mut cur_basis = BokutShiaoHecke::new(cur_strands, h.clone());

    for (step_idx, factor) in factors.iter().enumerate() {
        let mut next = FreeAlg::zero();
        if !factor.d.is_zero() {
            next.add_scaled_assign(&state, &factor.d);
        }
        if !factor.c.is_zero() {
            for (w, coeff) in state.terms() {
                let mut w_ext = Vec::with_capacity(w.len() + 1);
                w_ext.extend_from_slice(w);
                w_ext.push(factor.gen);
                let red = cur_basis.reduce_word(&w_ext);
                let scaled = coeff.mul_val(&factor.c);
                next.add_scaled_assign(&red, &scaled);
            }
        }
        state = next;

        while cur_strands >= 2 {
            let top_gen = cur_strands - 2;
            let done_with_top = match last_seen[top_gen] {
                None => true,
                Some(last_idx) => last_idx <= step_idx,
            };
            if done_with_top {
                state = peel_top_layer_homogeneous(&state, top_gen, h, z_num, z_den);
                cur_strands -= 1;
                cur_basis = BokutShiaoHecke::new(cur_strands, h.clone());
            } else {
                break;
            }
        }
    }

    while cur_strands >= 2 {
        let top_gen = cur_strands - 2;
        state = peel_top_layer_homogeneous(&state, top_gen, h, z_num, z_den);
        cur_strands -= 1;
    }

    state.coeff(&[])
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::scalar::LaurentPoly;
    use crate::temperley_lieb::TemperleyLiebBasis;

    #[test]
    fn tower_peeling_matches_ocneanu_and_temperley_lieb_loop_trace() {
        type L = LaurentPoly<i64>;
        let h = L::h();
        let q = L::q();
        let delta = L::delta_two();

        // Work with unnormalized z * delta so everything stays in LaurentPoly<i64> without division:
        // Actually test z as an arbitrary LaurentPoly<i64>, e.g. z = q^2 - 1, against BokutShiaoHecke::ocneanu_trace!
        let z = &(&q * &q) - &L::one();
        let factors = vec![
            LinearFactor::sigma(0),
            LinearFactor::sigma_inv(1, &h),
            LinearFactor::sigma(2),
            LinearFactor::sigma(0),
            LinearFactor::sigma_inv(1, &h),
            LinearFactor::sigma(3),
            LinearFactor::sigma(2),
        ];

        let mut acc = StreamingHeckeAccumulator::new(5, h.clone());
        for f in &factors {
            acc.push_linear(f);
        }
        let elem = acc.into_state();

        let (peeled_trace, supports) = peel_tower_trace(&elem, 5, &h, &z);
        assert_eq!(supports.len(), 5);
        assert!(supports[4] <= 1);

        let streamed_trace = streaming_markov_trace(&factors, 5, &h, &z);
        let direct_trace = BokutShiaoHecke::new(5, h.clone()).ocneanu_trace(&elem, &z);
        assert_eq!(peeled_trace, direct_trace);
        assert_eq!(streamed_trace, direct_trace);

        // Also verify exact Temperley-Lieb loop closure compatibility:
        // Under sigma_i |-> q*1 - e_i, tr_loop(pi_TL(x)) = delta^n * tr_M(x) at z_TL = q^3 / (q^2 + 1)
        // Clearing denominators: delta^5 * tr_M(x)|_{z = q - 1/delta} => test on degree-2 word in H_3:
        let tl3 = TemperleyLiebBasis::with_hecke_projection(3, q.clone()).unwrap();
        let s0 = FreeAlg::<usize, L>::generator(0);
        let s1 = FreeAlg::<usize, L>::generator(1);
        let word_h3 = &(&s0 * &s1) * &s0; // trefoil/Hopf 3-crossing word: s0 s1 s0
        // tr_loop(pi_TL(s0 s1 s0)):
        // s0 s1 s0 = s0^2-like after Markov? Wait: tr_M(s0 s1 s0) = tr_M(s1 s0^2) = tr_M(s1(h s0 + 1)) = h z^2 + z!
        // Multiply by delta^3: h * (z*delta)^2 * delta + (z*delta) * delta^2 where z*delta = q*delta - 1 = q^2!
        // Look: z_TL * delta = (q - 1/delta)*delta = q*(q + q^-1) - 1 = q^2!!
        // So delta^3 * tr_M(s0 s1 s0) = h * q^4 * delta + q^2 * delta^2!
        let z_times_delta = &q * &q;
        let expected_loop = &(&(&h * &z_times_delta.pow_u32(2)) * &delta)
            + &(&z_times_delta * &delta.pow_u32(2));
        assert_eq!(tl3.loop_trace_of(&word_h3), expected_loop);
    }
}
