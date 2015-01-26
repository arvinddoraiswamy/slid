/* http://iamtgc.com/selectively-statically-compile-and-link-nix-binaries/ */
#include <stdio.h>
#include <math.h>

void calc(){
    float d= cos(90);
    printf("cosine of 90 is %f", d);
}

int main() {
    calc();
}
