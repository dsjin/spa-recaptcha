<template>
  <div>
    <re-captcha
      :siteKey="recaptcha"
      @verify="verify"
      @expire="expiredCallback"
      @fail="errorCallback"
      @token="receiveToken"
      ref="recaptcha"
    />
    <button
      @click="invoke"
    >
      Invoke The Challenge
    </button>
    <button
      @click="getToken"
    >
      Get Token
    </button>
    <div>
      {{ token }}
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import ReCaptcha from '@/components/ReCaptcha.vue'
import config from '@/config'
export default Vue.extend({
  name: 'SendForm',
  components: {
    ReCaptcha
  },
  data () {
    return {
      token: '',
      recaptcha: config.recaptcha
    }
  },
  methods: {
    verify (response: string) {
      console.log(response)
    },
    expiredCallback () {
      console.log('expiredCallback')
    },
    errorCallback (error: any) {
      console.log('errorCallback')
      console.log(error)
    },
    invoke () {
      // (this.$refs.recaptcha as any).execute()
      this.$root.$emit('recaptcha.invoke')
    },
    getToken () {
      // this.token = (this.$refs.recaptcha as any).token()
      // if (!this.token) {
      //   this.token = 'Please challenge once agian'
      // }
      this.$root.$emit('recaptcha.token')
    },
    receiveToken (token: string) {
      this.token = token
      if (!token) {
        this.token = 'Please challenge once agian'
      }
    }
  }
})
</script>

<style>
</style>
