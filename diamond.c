#include <string.h>
#include <stdlib.h>
#include <stdio.h>

void print_diamond(char start) {
    int width = (start - 'A') * 2 + 1;
    char list[width];

    for(int i = -width/2; i <= width/2; ++i) {
        memset(list,' ', sizeof(list));
        list[abs(i)] = start - abs(i);
        list[(width - 1) - abs(i)] = start - abs(i);
        printf("%s\n",list);
    }
}

int main (int argc, char const *argv[]) {
    if(argc <= 1) {
        print_diamond('Z');
    } else {
        print_diamond((char)argv[1][0]);
    }
    return 0;
}
