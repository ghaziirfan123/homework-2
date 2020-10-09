int main() {
    int x1, y1, n1, x2, y2, n2, x, y;
    scanf("%d", &x1);
    scanf("%d", &y1);
    scanf("%d", &n1);
    scanf("%d", &x2);
    scanf("%d", &y2);
    scanf("%d", &n2);

    for (x = -10; x <= 10; x++) {
        for (y = -10; y <= 10; y++) {
            if (x1 * x + y1 * y == n1 && x2 * x + y2 * y == n2) {
                printf("%d %d\n", x, y);
                return 0;
            }
        }
    }
    printf("No solution\n");
    return 0;
}