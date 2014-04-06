#include <string.h>
#include <stdlib.h>

void print_diamond(char start, int width) {
	char list[width+1];
	list[width] = 0;

	for(int i = -width/2; i <= width/2; ++i) {
		memset(list,' ', sizeof(list));
		list[abs(i)] = start - abs(i);
		list[(width - 1) - abs(i)] = start - abs(i);
		printf("%s\n",list);
	}
}

int main(void) {
	print_diamond('Z', 19);
	return 0;
}