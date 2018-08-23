#ifndef USGOV_4fe977c8d0a53583dece022923973911480285192b477133789486114bfa3454
#define USGOV_4fe977c8d0a53583dece022923973911480285192b477133789486114bfa3454

#include "event.h"
#include <vector>
#include "types.h"
#include "message.h"
#include "unique_id_generator.h"

namespace simulation {

    class message_event : public event {

        using t_t = types::t_t;
        using uid_t = unique_id_generator::uid_t;

        public:
            message_event(t_t time, message m, uid_t from_node_id, uid_t to_node_id): m(m), from_node_id(from_node_id), to_node_id(to_node_id), event(time){};
        private:
            message m;
            uid_t from_node_id;
            uid_t to_node_id;
            virtual void main_event() = 0;

    };

}

#endif
