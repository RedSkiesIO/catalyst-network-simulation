#ifndef USGOV_53559ef33875635354be7b372107dda04150c38fdfd558e338b3fb2a40f824b2
#define USGOV_53559ef33875635354be7b372107dda04150c38fdfd558e338b3fb2a40f824b2

#include "event.h"
#include <queue>
#include <vector>
#include "types.h"

namespace simulation{
    class scheduler {
            
        public:
            using t_t = types::t_t;
            scheduler(t_t et) : end_time(et), time (0), event_queue () {}
            void run ();
            void stop();
            t_t get_time();
            void schedule_event (event *);
            void schedule_event(std::vector<event *> new_events);
            
        private: 
            bool exit_called = false;
            t_t end_time;
            t_t time;
        
        protected:
            std::priority_queue<event*, std::vector<event *, std::allocator<event*> >, event_comparator> event_queue;
    };
}


#endif