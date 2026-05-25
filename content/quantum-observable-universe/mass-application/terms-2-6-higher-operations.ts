import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:terms-2-6-higher-operations",
  title:
    "Terms 2 and 6 as higher Gerstenhaber / cup-product operations on the spectral sequence",
  lean: {
    ref: "qou:QOU.BraidKnot.terms_2_6_higher_operations",
    validation: "not_checked",
  },
  uses: ["prop:spectral-sequence-h3-explicit"],
  tags: [
    "spectral-sequence",
    "hochschild",
    "habiro",
    "colored-jones",
    "kashaev",
    "wedderburn",
    "cup-product",
    "higher-operations",
    "term-2",
    "term-6",
  ],
});
