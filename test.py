from gskit.examples.absucl import ABSUCL
from gskit.framework import CRS

crs = CRS.new_sound()
absucl = ABSUCL(crs)

aa_sk, aa_pk = absucl.aa_setup()

absucl.add_vk_attr("ASD", aa_pk)

u_sk, u_pk = absucl.user_keygen()

asd_attr = absucl.attr_keygen(u_sk * absucl.g, "ASD", aa_sk)

absucl.sign("Wena wena", "ASD", u_sk, {"ASD": asd_attr}, 4)
