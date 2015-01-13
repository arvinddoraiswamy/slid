/* http://iamtgc.com/selectively-statically-compile-and-link-nix-binaries/ */

#include <stdio.h>
#include <math.h>

void calc(){
        float d= cos(90);
        printf("square root of 4 is %f", d);
}

int main() {
    calc();
}

