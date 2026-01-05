// the reduced state is when all the white and yellow faces are facing the same axis
// and the edges in the middle have all green and blue faces facing green or blue
// the cube is represented with a single 64 int when in this reduced state
// the allowed move set is this state is: U U' U2 D D' D2 R2 L2 F2 B2

// this file cotains a set of utility functions to translate from state to state in this reduced form
// it also contains what the solved state of the cube should be

// Layers:
/**
 *  Top:       Middle:     Bottom:
 *      B     |     B     |     B     
 *    0 0 1   |   0 x 1   |   4 4 5   
 *  L 1 x 2 R | L x x x R | L 5 x 6 R 
 *    2 3 3   |   2 x 3   |   6 7 7   
 *      F     |     F     |     F     
*/

#include <cstdint>
using namespace std;

static const uint64_t SOLVED = 64452025298634376L; // the solved state of the cube in reduced form (11100100 111110101100011010001000 111110101100011010001000 in binairy)

static const int CORNER_OFFSET = 0;
static const int CORNER_DATA_WIDTH = 3;
static const int CORNER_DATA_MASK = 0b111;

static const int EDGE_OFFSET = 24;
static const int EDGE_DATA_WIDTH = 3;
static const int EDGE_DATA_MASK = 0b111;

static const int SPECIAL_EDGE_OFFSET = 48;
static const int SPECIAL_EDGE_DATA_WIDTH = 2;
static const int SPECIAL_EDGE_DATA_MASK = 0b11;

static const int DATA_SIZE = 64;

/**
 * swap two pieces in the state
 * cycles 1->2->1 (swaps positions)
 */
uint64_t swap (uint64_t state, int group_offset, int group_data_width, int group_data_mask, int index1, int index2) {
    //compute the positions for each index
    int pos1 = ((group_offset+index1)*group_data_width);
    int pos2 = ((group_offset+index2)*group_data_width);

    // get the bits at each index position
    int bit_set1 = (state >> pos1) & group_data_mask;
    int bit_set2 = (state >> pos2) & group_data_mask;

    int difference = bit_set1 ^ bit_set2; // compute the bit difference between the two numbers
    int mask = difference << pos1 | difference << pos2; // generate the mask to xor with the state

    return state ^ mask;
}

/**
 * swap 4 pieces in the state
 * cycles from 1->2->3->4->1 (2 := 1, 3 := 2, 4 := 3, 1 := 4)
 */
uint64_t swap (uint64_t state, int group_offset, int group_data_width, int group_data_mask, int index1, int index2, int index3, int index4) {
    //compute the positions for each index
    int pos1 = ((group_offset+index1)*group_data_width);
    int pos2 = ((group_offset+index2)*group_data_width);
    int pos3 = ((group_offset+index3)*group_data_width);
    int pos4 = ((group_offset+index4)*group_data_width);

    // get the bits at each index position
    int bit_set1 = (state >> pos1) & group_data_mask;
    int bit_set2 = (state >> pos2) & group_data_mask;
    int bit_set3 = (state >> pos3) & group_data_mask;
    int bit_set4 = (state >> pos4) & group_data_mask;

    // all the changes that need to happen during xor opperation
    int diff1 = bit_set1 ^ bit_set2;
    int diff2 = bit_set2 ^ bit_set3;
    int diff3 = bit_set3 ^ bit_set4;
    int diff4 = bit_set4 ^ bit_set1;

    int mask = diff1 << pos2 | diff2 << pos3 | diff3 << pos4 | diff4 << pos1; // mask to xor with state

    return state ^ mask;
}