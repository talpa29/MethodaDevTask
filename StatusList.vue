<template>
  <div class="jumbotron vertical-center">
    <div class="container">
      <div class="row">
        <div class="col-sm-12">
          <h1 class="text-center bg-primary text-white" style="border-radius:10px"> Status List </h1>
          <hr><br> 

          <!--Alarat Message-->
          <button type="button" class="btn btn-success btn-sm" v-b-modal.status-modal>Add Status</button>
          <br><br>
          <table class="table table-hover">
            <!--Table Head-->
            <thead>
              <tr>
                <!--Table Header cells-->
                <th scope="col">Name</th>
                <th scope="col">Type</th>
                <th scope="col">Action</th>
              </tr>
            </thead>
            <tbody>
                  <tr v-for="status, index in status" :key="index">
                  <td>{{status.name}}</td>
                  <td>{{status.type}}</td>
                  <td>
                    <div class="btn-group" role="group">
                      <button
                        type="button"
                        class="btn btn-info btn-sm"
                        v-b-modal.status-update-modal
                        @click="editStatus(status)"> Update </button>
                      <button type="button" class="btn btn-danger btn-sm" @click="deleteStatus(status)">Delete</button>
                    </div>
                  </td>
              </tr>
            </tbody>
          </table>
        </div>


        <div class="col-sm-12">
          <h1 class="text-center bg-primary text-white" style="border-radius:10px"> Transition List </h1>
          <hr><br> 

          <!--Alarat Message-->
          <button type="button" class="btn btn-success btn-sm" v-b-modal.transition-modal>Add Transition</button>
          <br><br>
          <table class="table table-hover">
            <!--Table Head-->
            <thead>
              <tr>
                <!--Table Header cells-->
                <th scope="col">Name</th>
                <th scope="col">From</th>
                <th scope="col">To</th>
              </tr>
            </thead>
            <tbody>
                  <tr v-for="transition, index in transition" :key="index">
                  <td>{{transition.name}}</td>
                  <td>{{transition.from}}</td>
                  <td>{{transition.to}}</td>
                  <td>
                    <div class="btn-group" role="group">
                      <button
                        type="button"
                        class="btn btn-info btn-sm"
                        v-b-modal.transition-update-modal
                        @click="editTransition(transition)"> Update </button>
                      <button type="button" class="btn btn-danger btn-sm" @click="deleteTransition(transition)">Delete</button>
                    </div>
                  </td>
              </tr>
            </tbody>
          </table>
        </div>


      </div>
      <!--First Modal-->
      <b-modal ref="addStatusModal"
             id="status-modal"
             title="Add a new status"
             hide-backdrop hide-footer>
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-name-group"
                    label="name:"
                    label-for="form-name-input">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="addStatusForm.name"
                        required
                        placeholder="Enter name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-type-group"
                      label="type:"
                      label-for="form-type-input">
            <b-form-input id="form-type-input"
                          type="text"
                          v-model="addStatusForm.type"
                          required
                          placeholder="Enter type">
            </b-form-input>
        </b-form-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
    <!--End of First Modal-->

    <!-- Start of Modal 2 -->
    <b-modal ref="editStatusModal"
          id="status-update-modal"
          title="Update" hide-backdrop
          hide-footer>
    <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      
    <b-form-group id="form-name-edit-group"
                  label="name:"
                  label-for="form-name-edit-input">
        <b-form-input id="form-name-edit-input"
                      type="text"
                      v-model="editForm.name"
                      required
                      placeholder="Enter name">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-type-edit-group"
                    label="type:"
                    label-for="form-type-edit-input">
          <b-form-input id="form-type-edit-input"
                        type="text"
                        v-model="editForm.type"
                        required
                        placeholder="Enter type">
          </b-form-input>
        </b-form-group>

      <b-button-group>
        <b-button type="submit" variant="outline-info">Update</b-button>
        <b-button type="reset" variant="outline-danger">Cancel</b-button>
      </b-button-group>
    </b-form>
  </b-modal>
  <!-- end of modal 2 -->


   <!--First Modal Transition-->
   <b-modal ref="addTransitionModal"
             id="transition-modal"
             title="Add a new transition"
             hide-backdrop hide-footer>
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-name-group"
                    label="name:"
                    label-for="form-name-input">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="addTransitionForm.name"
                        required
                        placeholder="Enter name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-from-group"
                      label="from:"
                      label-for="form-from-input">
            <b-form-input id="form-from-input"
                          type="text"
                          v-model="addTransitionForm.from"
                          required
                          placeholder="Enter from">
            </b-form-input>
        </b-form-group>
        <b-form-group id="form-to-group"
                      label="to:"
                      label-for="form-to-input">
            <b-form-input id="form-to-input"
                          type="text"
                          v-model="addTransitionForm.to"
                          required
                          placeholder="Enter to">
            </b-form-input>
        </b-form-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
    <!--End of First Modal-->

    <!-- Start of Modal 2 -->
    <b-modal ref="editTransitionModal"
          id="transition-update-modal"
          title="Update" hide-backdrop
          hide-footer>
    <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      
    <b-form-group id="form-name-edit-group"
                  label="name:"
                  label-for="form-name-edit-input">
        <b-form-input id="form-name-edit-input"
                      type="text"
                      v-model="editFormT.name"
                      required
                      placeholder="Enter name">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-type-edit-group"
                    label="from:"
                    label-for="form-from-edit-input">
          <b-form-input id="form-from-edit-input"
                        type="text"
                        v-model="editFormT.from"
                        required
                        placeholder="Enter from">
          </b-form-input>

        </b-form-group>
        <b-form-group id="form-type-edit-group"
                    label="to:"
                    label-for="form-to-edit-input">
          <b-form-input id="form-to-edit-input"
                        type="text"
                        v-model="editFormT.to"
                        required
                        placeholder="Enter to">
          </b-form-input>
        </b-form-group>

      <b-button-group>
        <b-button type="submit" variant="outline-info">Update</b-button>
        <b-button type="reset" variant="outline-danger">Cancel</b-button>
      </b-button-group>
    </b-form>
  </b-modal>


    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default{
  data() {
    return {
      status: [],
      addStatusForm: {
        name: '',
        type: '',
    },
    editForm: {
      id: '',
      name: '',
      type: '',
    },
    transition: [],
      addTransitionForm: {
        name: '',
        from: '',
        to: '',
    },
    editFormT: {
      id: '',
      name: '',
      from: '',
      to: '',
    },
    };
  },


  methods:{
    getStatus(){
      const path = 'http://localhost:5000';
      axios.get(path)
      .then((res) => {
        this.status = res.data.Statuses;
        this.transition = res.data.Transitions;
      })
      .catch((err) => {
        console.error(err);
      });
    },
    // POST function
    addStatus(payload) {
      const path = 'http://localhost:5000';
      axios.post(path, payload)
      .then(() => {
        this.getStatus();
      })
      .catch((err) => {
        console.error(err);
        this.getStatus();
      });
    },
    initForm(){
      this.addStatusForm.name = ''
      this.addStatusForm.type = ''
      this.editForm.id = ''
      this.editForm.name = ''
      this.editForm.type = ''
      this.addTransitionForm.name = ''
      this.addTransitionForm.from = ''
      this.addTransitionForm.to = ''
      this.editFormT.id = ''
      this.editFormT.name = ''
      this.editFormT.type = ''
      this.editFormT.to = ''
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addStatusModal.hide();
      const payload = {
        name: this.addStatusForm.name + this.addTransitionForm.name,
        type: this.addStatusForm.type,
        from: this.addTransitionForm.from,
        to: this.addTransitionForm.to,
      };
      this.addStatus(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$ref.addStatusModal.hide();
      this.$ref.addTransitionModal.hide();
      this.initForm();
    },

    onSubmitUpdate(e) {
      e.preventDefault();
      this.$refs.editStatusModal.hide();
      this.$refs.editTransitionModal.hide();
      const payload = {
        name: this.editForm.name + this.editFormT.name,
        type: this.editForm.type,
        from: this.editFormT.from,
        to: this.editFormT.to,
      };
      this.updateStatus(payload, this.editForm.id, this.editFormT.id);
  },

    updateStatus(payload, statusID, transitionID) {
      if (transitionID != ''){
        const path = `http://localhost:5000/${transitionID}`;
      }
      else{
        const path = `http://localhost:5000/${statusID}`;
      }       
      axios.put(path, payload)    
        .then(() => {
          this.getStatus();
        })
        .catch((error) => {
          console.error(error);
          this.getGames();
        });
},
 // Handle Update Button 
 editStatus(status) {
  this.editForm = status;
},

editTransition(transition) {
  this.editFormT = transition;
},


onResetUpdate(e) {
  e.preventDefault();
  this.$refs.editStatusModal.hide();
  this.$refs.editTransitionModal.hide();
  this.initForm();
  this.getStatus(); 
},

removeStatus(statusID) {
  const path = `http://localhost:5000/${statusID}`;
  axios.delete(path)
    .then(() => {
      this.getStatus();
    })
    .catch((error) => {
      // eslint-disable-next-line
      console.error(error);
      this.getStatus();
    });
},

// Handle Delete Button
deleteStatus(status) {
  this.removeStatus(status.id);
},

deleteTransition(transition){
  this.removeStatus(transition.id);
},

    
  },
  created() {
    this.getStatus();
  },
};
</script>

