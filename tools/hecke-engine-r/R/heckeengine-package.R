#' heckeengine: QOU Hecke-engine Gram + Markov-trace primitives
#'
#' R bindings to the QOU `hecke-engine` Rust crate via extendr.
#' Exposes the Iwahori-Hecke H_3(q) Gram matrix, Markov-trace
#' weights, and substrate-q convenience functions.
#'
#' @section Functions:
#'   * `qou_version()`         — package version
#'   * `qou_markov_z(q)`       — z = q^3 / (q^2 + 1)  (trace convention D)
#'   * `qou_hecke_h(q)`        — h = q - q^{-1}
#'   * `qou_trace_weights(q)`  — 6-element NF-basis weights
#'   * `qou_gram_matrix(q)`    — 6x6 Gram matrix
#'   * `qou_gram_det(q)`       — Gram determinant
#'
#' @section Example:
#' \preformatted{
#'   library(heckeengine)
#'   q0 <- 1.10998
#'   qou_markov_z(q0)
#'   G <- qou_gram_matrix(q0)
#'   stopifnot(dim(G) == c(6, 6))
#'   det(G)  # base-R det; should match qou_gram_det(q0)
#' }
#'
#' @keywords internal
"_PACKAGE"
