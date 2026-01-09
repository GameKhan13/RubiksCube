#include "moves.cpp"
#include <unordered_map>
#include <string>
#include <vector>
#include <list>

string file_name = "map.txt";

struct CallData
{
    uint64_t state;
    bool u, d, f, b, r, l;
};


void generateMap(unordered_map<uint64_t, uint64_t>* map, int depth) {
    list<CallData*>* paths = new list<CallData*>();
    paths->push_back(new CallData{SOLVED, false, false, false, false, false, false});

    while(depth > 0 && paths->size() > 0) {
        list<CallData*>* new_paths = new list<CallData*>();
        for(CallData* path : *paths) {
            new_paths->merge(*generate(map, path->state, path->u, path->d, path->f, path->b, path->r, path->l));
        }
        paths = new_paths;
        depth-=1;
    }
}

list<CallData*>* generate(unordered_map<uint64_t, uint64_t>* map, uint64_t state, bool u, bool d, bool f, bool b, bool r, bool l) {
    list<CallData*>* data = new list<CallData*>;

    uint64_t result;
    if (!u) {
        result = U(state);
        if((*map)[result] == 0) {
            (*map)[result] = state;
            data->push_back(new CallData{result, true, d, false, false, false, false});
        }
        
        result = UP(state);
        if((*map)[result] == 0) {
            (*map)[result] = state;
            data->push_back(new CallData{result, true, d, false, false, false, false});
        }

        result = U2(state);
        if((*map)[result] == 0) {
            (*map)[result] = state;
            data->push_back(new CallData{result, true, d, false, false, false, false});
        }
    }

    if (!d) {
        result = D(state);
        if((*map)[result] == 0) {
            (*map)[result] = state;
            data->push_back(new CallData{result, u, true, false, false, false, false});
        }
        
        result = DP(state);
        if((*map)[result] == 0) {
            (*map)[result] = state;
            data->push_back(new CallData{result, u, true, false, false, false, false});
        }

        result = D2(state);
        if((*map)[result] == 0) {
            (*map)[result] = state;
            data->push_back(new CallData{result, u, true, false, false, false, false});
        }
    }

    if (!f) {
        result = F2(state);
        if((*map)[result] == 0) {
            (*map)[result] = state;
            data->push_back(new CallData{result, false, false, true, b, false, false});
        }
    }

    if (!b) {
        result = B2(state);
        if((*map)[result] == 0) {
            (*map)[result] = state;
            data->push_back(new CallData{result, false, false, f, true, false, false});
        }
    }

    if (!r) {
        result = R2(state);
        if((*map)[result] == 0) {
            (*map)[result] = state;
            data->push_back(new CallData{result, false, false, false, false, true, l});
        }
    }

    if (!l) {
        result = L2(state);
        if((*map)[result] == 0) {
            (*map)[result] = state;
            data->push_back(new CallData{result, false, false, false, false, r, true});
        }
    }
}

void writeMapToFile(unordered_map<uint64_t, uint64_t>* map) {

}

unordered_map<uint64_t, uint64_t>* readMapFromFile () {

}