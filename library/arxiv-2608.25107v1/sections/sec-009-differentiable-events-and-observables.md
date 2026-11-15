---
doc_id: arxiv-2608.25107v1
doc_title: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples"
section_id: sec-009-differentiable-events-and-observables
section_title: "Differentiable events and observables"
section_number: null
pages: 7-7
source_pdf: 2608.25107v1.pdf
source_sha256: 6dca8b99a1f32db4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 1.0
doc_brief: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples — 19 sections: ADoNIS: A Differentiable generatOr; Introduction; Differentiable programming in part"
---
[]{#sec:adonis_events label="sec:adonis_events"}

The result of the generation is a bank in which every event carries, alongside its final-state kinematics, the records of Secs. [\[sec:adonis_nucleus\]](#sec:adonis_nucleus){reference-type="ref" reference="sec:adonis_nucleus"}--[\[sec:adonis_cascade\]](#sec:adonis_cascade){reference-type="ref" reference="sec:adonis_cascade"} that render its weight $w_i(\bm\theta)$ of Eq. [\[eq:adonis_weight\]](#eq:adonis_weight){reference-type="ref" reference="eq:adonis_weight"} an exact, differentiable function of the physics parameters. Differentiability is thus a property of each stored event individually: for any event one can ask, and answer exactly, how its weight responds to any physics parameter.

This event-by-event differentiability is what makes the downstream analysis differentiable for free. Physics observables are built from the events by operations that do not depend on $\bm\theta$: a signal or topology definition selects events by their final state, a choice of kinematic variable maps each event to an axis value, and a binning assigns each event to a bin. None of these touches the weights, so a binned prediction is simply the sum of the differentiable per-event weights falling in each bin, $$\label{eq:adonis_binned}
m_b(\bm\theta) = \sum_{i \in b} w_i(\bm\theta),
\qquad
\frac{\partial m_b}{\partial\bm\theta} = \sum_{i \in b}
\frac{\partial w_i}{\partial\bm\theta}.$$ The gradient of any histogram, and therefore of any differentiable downstream statistic built from it, is obtained by propagating the gradients of the weights through the same selection and binning. Changing the signal definition, the observable, or the bin edges changes which events enter each sum but not the differentiability of the result. In sum, an analysis is free to define its observables however it wishes and retains exact gradients with respect to the physics parameters throughout.

Nothing in Eq. [\[eq:adonis_binned\]](#eq:adonis_binned){reference-type="ref" reference="eq:adonis_binned"} requires an event to belong to a single bin. The sum may equally be taken over a weight $\alpha_{ib}$ that spreads each event across bins, $m_b = \sum_i \alpha_{ib}\,w_i(\bm\theta)$, and the gradient follows unchanged. When an event's observable is known only to within a reconstruction uncertainty, that uncertainty can therefore be carried into the prediction as a soft assignment rather than collapsed into a hard choice of bin.
