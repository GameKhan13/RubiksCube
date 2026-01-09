#include "cube.cpp"

/**
 * Entire moveset required to solve the cube when in reduced form (removes 8 unnessesary moves to search)
 * Improves efficiency of search by reducing the cube to a single 64 bit number for easy comparisions and look-ups
 * And reduces the number of moves that need to be searched through from 18 to 10
 * Technically U2, UP, D2 and DP dont need to be included here but they are
 */

uint64_t F2 (uint64_t state) {
    state = swap(state, CORNER_OFFSET, CORNER_DATA_WIDTH, CORNER_DATA_MASK, 2, 7);
    state = swap(state, CORNER_OFFSET, CORNER_DATA_WIDTH, CORNER_DATA_MASK, 3, 6);
    state = swap(state, EDGE_OFFSET, EDGE_DATA_WIDTH, EDGE_DATA_MASK, 3, 7);
    state = swap(state, SPECIAL_EDGE_OFFSET, SPECIAL_EDGE_DATA_WIDTH, SPECIAL_EDGE_DATA_MASK, 2, 3);
    return state;
}

uint64_t B2 (uint64_t state) {
    state = swap(state, CORNER_OFFSET, CORNER_DATA_WIDTH, CORNER_DATA_MASK, 0, 5);
    state = swap(state, CORNER_OFFSET, CORNER_DATA_WIDTH, CORNER_DATA_MASK, 1, 4);
    state = swap(state, EDGE_OFFSET, EDGE_DATA_WIDTH, EDGE_DATA_MASK, 0, 4);
    state = swap(state, SPECIAL_EDGE_OFFSET, SPECIAL_EDGE_DATA_WIDTH, SPECIAL_EDGE_DATA_MASK, 0, 1);
    return state;
}

uint64_t R2 (uint64_t state) {
    state = swap(state, CORNER_OFFSET, CORNER_DATA_WIDTH, CORNER_DATA_MASK, 1, 7);
    state = swap(state, CORNER_OFFSET, CORNER_DATA_WIDTH, CORNER_DATA_MASK, 3, 5);
    state = swap(state, EDGE_OFFSET, EDGE_DATA_WIDTH, EDGE_DATA_MASK, 2, 6);
    state = swap(state, SPECIAL_EDGE_OFFSET, SPECIAL_EDGE_DATA_WIDTH, SPECIAL_EDGE_DATA_MASK, 1, 3);
    return state;
}

uint64_t L2 (uint64_t state) {
    state = swap(state, CORNER_OFFSET, CORNER_DATA_WIDTH, CORNER_DATA_MASK, 0, 6);
    state = swap(state, CORNER_OFFSET, CORNER_DATA_WIDTH, CORNER_DATA_MASK, 2, 4);
    state = swap(state, EDGE_OFFSET, EDGE_DATA_WIDTH, EDGE_DATA_MASK, 1, 5);
    state = swap(state, SPECIAL_EDGE_OFFSET, SPECIAL_EDGE_DATA_WIDTH, SPECIAL_EDGE_DATA_MASK, 0, 2);
    return state;
}

uint64_t U (uint64_t state) {
    state = swap(state, CORNER_OFFSET, CORNER_DATA_WIDTH, CORNER_DATA_MASK, 0, 1, 3, 2);
    state = swap(state, EDGE_OFFSET, EDGE_DATA_WIDTH, EDGE_DATA_MASK, 0, 2, 3, 1);
    return state;
}

uint64_t UP (uint64_t state) {
    state = swap(state, CORNER_OFFSET, CORNER_DATA_WIDTH, CORNER_DATA_MASK, 0, 2, 3, 1);
    state = swap(state, EDGE_OFFSET, EDGE_DATA_WIDTH, EDGE_DATA_MASK, 0, 1, 3, 2);
    return state;
}

uint64_t U2 (uint64_t state) {
    state = swap(state, CORNER_OFFSET, CORNER_DATA_WIDTH, CORNER_DATA_MASK, 0, 3);
    state = swap(state, CORNER_OFFSET, CORNER_DATA_WIDTH, CORNER_DATA_MASK, 1, 2);
    state = swap(state, EDGE_OFFSET, EDGE_DATA_WIDTH, EDGE_DATA_MASK, 0, 3);
    state = swap(state, EDGE_OFFSET, EDGE_DATA_WIDTH, EDGE_DATA_MASK, 1, 2);
    return state;
}

uint64_t D (uint64_t state) {
    state = swap(state, CORNER_OFFSET, CORNER_DATA_WIDTH, CORNER_DATA_MASK, 4, 5, 7, 6);
    state = swap(state, EDGE_OFFSET, EDGE_DATA_WIDTH, EDGE_DATA_MASK, 4, 6, 7, 5);
    return state;
}

uint64_t DP (uint64_t state) {
    state = swap(state, CORNER_OFFSET, CORNER_DATA_WIDTH, CORNER_DATA_MASK, 4, 6, 7, 5);
    state = swap(state, EDGE_OFFSET, EDGE_DATA_WIDTH, EDGE_DATA_MASK, 4, 5, 7, 6);
    return state;
}

uint64_t D2 (uint64_t state) {
    state = swap(state, CORNER_OFFSET, CORNER_DATA_WIDTH, CORNER_DATA_MASK, 4, 7);
    state = swap(state, CORNER_OFFSET, CORNER_DATA_WIDTH, CORNER_DATA_MASK, 5, 6);
    state = swap(state, EDGE_OFFSET, EDGE_DATA_WIDTH, EDGE_DATA_MASK, 4, 7);
    state = swap(state, EDGE_OFFSET, EDGE_DATA_WIDTH, EDGE_DATA_MASK, 5, 6);
    return state;
}
