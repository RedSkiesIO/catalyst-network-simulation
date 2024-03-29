#ifndef USGOV_2b958752d6f9e516e215760786938a831ed91807faa25b7de3ffdf2e50e0c873
#define USGOV_2b958752d6f9e516e215760786938a831ed91807faa25b7de3ffdf2e50e0c873

#include "Ilatency.h"
#include "types.h"

namespace simulation{
    class single_latency : public virtual Ilatency{
        using t_t = types::t_t;
        using uid_t = types::uid_t;
        public:
            single_latency(){};
            t_t get_latency(uid_t from_node_id, uid_t to_node_id);

    };

}

#endif

